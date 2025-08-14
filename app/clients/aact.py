# Data source client — AACT (stub)
#
# What this file does:
#   • Returns a tiny list of trial dicts shaped for the pipeline demo.
#   • Meant to be swapped later for a real Postgres/AACT SQL query.
#   • Each item should at least have: nct_id, title, abstract (strings).

def fetch_recent():
    return [
        {"nct_id": "NCT00000000", "title": "Phase 3 RCT in X",         "abstract": "..."},
        {"nct_id": "NCT00000001", "title": "Phase 3 OS superiority",   "abstract": "..."},
    ]