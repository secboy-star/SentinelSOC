"""Emit a reproducible synthetic SSH log for the local collection demo.

Run: python3 scripts/replay_synthetic_auth.py > synthetic-auth.jsonl
"""

import json
from datetime import datetime, timedelta, timezone


def main():
    start = datetime(2026, 1, 1, tzinfo=timezone.utc)
    attempts = [
        (second, "failure", "192.0.2.10", "synthetic-test")
        for second in range(0, 30, 5)
    ]
    attempts.append((40, "success", "198.51.100.20", "synthetic-admin"))
    for second, outcome, source_ip, user in attempts:
        print(json.dumps({
            "timestamp": (start + timedelta(seconds=second)).isoformat(),
            "service": "sshd",
            "outcome": outcome,
            "source_ip": source_ip,
            "user": user,
            "synthetic": True,
        }))


if __name__ == "__main__":
    main()
