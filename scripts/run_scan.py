# CLI helper — run a scan without starting the API (demo)
#
# What this file does:
#   • Executes one pipeline scan and prints the queued candidates.
#   • Useful for quick demos and for future cron/scheduler integration.
#
# Usage:
#   • python -m scripts.run_scan

from app.pipeline.scan_established import scan_once, CANDIDATES

if __name__ == "__main__":
    print({"queued": scan_once(), "candidates": CANDIDATES})
