"""Expose stale queue claims without changing research records or priorities."""
import argparse
import json
import re
from datetime import date
from pathlib import Path
try:
    from tools.validate_research import validate
except ModuleNotFoundError:
    from validate_research import validate


def audit_queue(text, records, today):
    results = []
    for line in text.splitlines():
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        if len(cells) != 9 or not cells[0].isdigit():
            continue
        ticker, action, due = cells[1], cells[6], cells[7]
        issues = []
        try:
            if date.fromisoformat(due) < today:
                issues.append('overdue')
        except ValueError:
            issues.append('invalid_due_date')
        record = records.get(ticker)
        if record is None:
            issues.append('missing_record')
        elif re.search(r'quote\s+(?:now\s+)?verified', action, re.I):
            if 'Two matching quote sources with different underlying origins are required' in validate(record)['blockers']:
                issues.append('quote_verification_contradicts_record')
        results.append({'ticker': ticker, 'due': due, 'next_action': action, 'issues': issues})
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--queue', type=Path, default=Path('journal/queue.md'))
    parser.add_argument('--records', type=Path, default=Path('journal/research'))
    parser.add_argument('--today', type=date.fromisoformat, default=date.today())
    args = parser.parse_args()
    records = {p.stem: json.loads(p.read_text()) for p in args.records.glob('*.json')}
    rows = audit_queue(args.queue.read_text(), records, args.today)
    print(json.dumps({'as_of': args.today.isoformat(), 'rows': rows,
                      'flagged_rows': sum(bool(row['issues']) for row in rows)}, indent=2))
    return int(any(row['issues'] for row in rows))


if __name__ == '__main__':
    raise SystemExit(main())
