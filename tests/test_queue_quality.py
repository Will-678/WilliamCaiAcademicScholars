import unittest
from datetime import date
from tools.queue_quality import audit_queue
from test_research_quality import complete_record

class QueueQualityTests(unittest.TestCase):
    def test_stale_verification_and_overdue_are_visible_without_mutation(self):
        queue = '| CIK | Ticker | Exchange | Sector | Stage | Last reviewed | Next action | Due | Reason |\n| 1 | ABC | NYSE | software | researched_watch | 2026-11-01 | Quote now verified | 2026-11-13 | old |'
        record = {'ticker': 'ABC', 'price': {'status': 'unconfirmed'}}
        before = repr(record)
        rows = audit_queue(queue, {'ABC': record}, date(2026, 11, 22))
        self.assertEqual(rows[0]['issues'], ['overdue', 'quote_verification_contradicts_record'])
        self.assertEqual(repr(record), before)

    def test_missing_record_is_not_silently_promoted(self):
        queue = '| 1 | XYZ | NYSE | software | researched_watch | 2026-11-22 | Read filing | 2026-11-22 | pending |'
        self.assertEqual(audit_queue(queue, {}, date(2026, 11, 22))[0]['issues'], ['missing_record'])

    def test_previous_close_with_documented_origins_is_not_a_contradiction(self):
        record = complete_record()
        queue = '| 1 | ABC | NYSE | software | researched_watch | 2026-11-22 | Quote now verified | 2026-11-22 | current |'
        rows = audit_queue(queue, {'ABC': record}, date(2026, 11, 22))
        self.assertNotIn('quote_verification_contradicts_record', rows[0]['issues'])
