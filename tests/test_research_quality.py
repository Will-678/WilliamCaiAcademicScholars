import copy
import importlib.util
import json
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def module(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / (name + ".py"))
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


screen = module("screen_universe")
quality = module("validate_research")
NOW = datetime(2026, 11, 6, 0, tzinfo=timezone.utc)


def frame_data():
    flow = dict(start="2025-01-01", end="2025-12-31", accn="TEST", entityName="Fixture Only")
    values = dict(revenue=200e6, revenue_base=150e6, net_income=20e6, ocf=30e6,
                  capex=10e6, assets=300e6, liabilities=100e6, equity=200e6)
    out = {k: {1: dict(flow, val=v)} for k, v in values.items()}
    out["revenue_base"][1].update(start="2023-01-01", end="2023-12-31")
    return out


def complete_record():
    sources = [
        dict(id="annual", document_id="annual-2025", origin="issuer", kind="annual_filing"),
        dict(id="quarter", document_id="quarter-2026", origin="issuer", kind="quarterly_filing"),
        dict(id="quote1", document_id="close-provider-one", origin="provider-one", kind="quote"),
        dict(id="quote2", document_id="close-provider-two", origin="provider-two", kind="quote"),
    ]
    for source in sources:
        source.update(url="https://example.org/" + source["id"], read_status="relevant_sections",
                      accessed_at="2026-11-05T18:00:00-05:00")
    price_time = "2026-11-05T16:00:00-05:00"
    return dict(schema_version=2, method_version="2.0", ticker="FIXTURE", exchange="NYSE", currency="USD",
                sector_model="nonfinancial", as_of="2026-11-05T18:30:00-05:00", status="attractive", confidence="high",
                thesis="Fixture thesis", counterthesis="Fixture counterargument", invalidation="Fixture trigger",
                sources=sources, checks={k: dict(passed=True, source_ids=["quarter"], note="Fixture relevant section")
                                        for k in quality.CHECKS},
                price=dict(value=100, currency="USD", as_of=price_time, status="previous_close",
                           last_completed_session="2026-11-05",
                           sources=[dict(source_id=k, value=100, currency="USD", as_of=price_time)
                                    for k in ("quote1", "quote2")]),
                scores=dict(business_quality=21, cash_generation_growth=16, financial_resilience=13,
                            valuation=26, catalysts_evidence=9), score_total=85,
                calculations={}, unresolved_critical_gaps=[])


class ScreenTests(unittest.TestCase):
    def test_missing_capex_never_becomes_zero(self):
        data = frame_data()
        data["capex"].clear()
        rows, excluded = screen.build_rows(data)
        self.assertEqual(rows, [])
        self.assertEqual(excluded["missing:capex"], 1)

    def test_explicit_zero_spending_is_valid(self):
        data = frame_data()
        data["capex"][1]["val"] = 0
        rows, excluded = screen.build_rows(data)
        self.assertEqual(len(rows), 1)
        self.assertAlmostEqual(rows[0]["fcf_margin"], .15)

    def test_different_cashflow_period_is_excluded(self):
        data = frame_data()
        data["ocf"][1]["end"] = "2025-09-30"
        self.assertEqual(screen.build_rows(data)[0], [])

    def test_different_balance_date_is_excluded(self):
        data = frame_data()
        data["assets"][1]["end"] = "2026-03-31"
        self.assertEqual(screen.build_rows(data)[0], [])

    def test_zero_assets_do_not_divide_by_zero(self):
        data = frame_data()
        data["assets"][1]["val"] = 0
        self.assertEqual(screen.build_rows(data)[0], [])

    def test_conflicting_revenue_does_not_rank(self):
        data = frame_data()
        data["revenue"][1]["conflicting_tags"] = True
        self.assertEqual(screen.build_rows(data)[0], [])

    def test_nan_is_excluded(self):
        data = frame_data()
        data["ocf"][1]["val"] = float("nan")
        self.assertEqual(screen.build_rows(data)[0], [])

    def test_empty_pass_list_writes_headers(self):
        with tempfile.TemporaryDirectory() as folder:
            screen.write_outputs([], {"passed": 0}, folder)
            self.assertIn("cik,name,revenue", (Path(folder) / "screen_latest.csv").read_text())
            self.assertEqual(json.loads((Path(folder) / "screen_metadata.json").read_text())["passed"], 0)

    def test_tiny_equity_does_not_inflate_roe(self):
        data = frame_data()
        data["equity"][1]["val"] = 1
        row = screen.build_rows(data)[0][0]
        self.assertIsNone(row["roe"])
        self.assertIn("roe_unusable", row["flags"])


class ResearchTests(unittest.TestCase):
    def test_complete_fixture_passes(self):
        self.assertTrue(quality.validate(complete_record(), NOW)["eligible_attractive"])

    def test_two_urls_with_one_data_origin_fail(self):
        record = complete_record()
        record["sources"][-1]["origin"] = "provider-one"
        result = quality.validate(record, NOW)
        self.assertFalse(result["valid"])
        self.assertTrue(any("different underlying origins" in b for b in result["blockers"]))

    def test_disagreeing_quote_fails(self):
        record = complete_record()
        record["price"]["sources"][1]["value"] = 120
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_future_quote_fails(self):
        record = complete_record()
        record["price"]["as_of"] = "2026-11-06T16:00:00-05:00"
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_stale_quote_fails(self):
        record = complete_record()
        record["price"]["as_of"] = "2026-10-01T16:00:00-04:00"
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_malformed_source_identity_fails_closed(self):
        record = complete_record()
        record["sources"][0]["id"] = ["not a string"]
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_later_source_is_not_point_in_time_evidence(self):
        record = complete_record()
        record["as_of"] = "2026-11-05T17:00:00-05:00"
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_missing_debt_check_blocks_attractive(self):
        record = complete_record()
        record["checks"]["balance_sheet_verified"]["passed"] = False
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_search_snippet_is_not_filing_evidence(self):
        record = complete_record()
        record["sources"][1]["read_status"] = "snippet"
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_score_sum_mismatch_fails(self):
        record = complete_record()
        record["score_total"] = 99
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_missing_score_must_not_keep_numeric_total(self):
        record = complete_record()
        record["scores"]["valuation"] = None
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_unavailable_record_is_valid_draft_not_promotion(self):
        record = json.loads((ROOT / "templates" / "research_record.json").read_text())
        result = quality.validate(record, datetime(2026, 11, 6, 12, tzinfo=timezone.utc))
        self.assertTrue(result["valid"], result)
        self.assertFalse(result["eligible_attractive"])
        self.assertTrue(result["blockers"])

    def test_cashflow_units_and_periods_must_match(self):
        op = dict(value=100, unit="USD_millions", period_start="2026-01-01", period_end="2026-09-30")
        cap = dict(op, value=20, unit="USD")
        with self.assertRaises(ValueError):
            quality.fcf(op, cap)

    def test_missing_cashflow_spending_raises(self):
        with self.assertRaises(ValueError):
            quality.fcf({"value": 100}, None)

    def test_cashflow_arithmetic_is_reconciled(self):
        record = complete_record()
        flow = dict(unit="USD_millions", period_start="2026-01-01", period_end="2026-09-30")
        record["calculations"]["fcf"] = dict(ocf=dict(flow, value=100), capex=dict(flow, value=20), value=95)
        self.assertFalse(quality.validate(record, NOW)["valid"])

    def test_annualized_scenario_includes_time(self):
        self.assertAlmostEqual(quality.annualized_scenario(100, 121, 0, 2), .1)


if __name__ == "__main__":
    unittest.main()
