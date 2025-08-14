# What this file does:
#   • Runs a single scan to build a review queue of “established” candidates.
#   • Flow: clients.fetch_recent() → extractor.extract() → evaluation.decide() → queue.
#   • Output: appends items to the in-memory CANDIDATES list and returns the total queued.
#
# How to extend later:
#   • Swap clients.aact.fetch_recent() for a real SQL query.
#   • Persist CANDIDATES to a DB, add PubMed/CT.gov clients, and enable C2.

from app.clients.aact import fetch_recent
from app.extractor.llm import extract
from app.evaluation.established import decide

# In-memory review queue shared by the API and CLI demo.
CANDIDATES: list[dict] = []

def scan_once() -> int:
    """Run one scan and queue trials that meet C1/C3; return total queued."""
    for item in fetch_recent():
        ex = extract(item)              # turn title/abstract into simple features
        ok, reasons = decide(ex)        # apply criteria rules
        if ok:
            CANDIDATES.append({"trial": item, "reasons": reasons})
    return len(CANDIDATES)