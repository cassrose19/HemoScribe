# Extractor — turns unstructured trial text into tiny features (demo)
#
# What this file does:
#   • Produces the minimal fields needed by the rules engine (C1/C3).
#   • Uses title heuristics for the demo; swap with LLM JSON later.
#
# Output keys:
#   • phase, is_rct, has_comparator, pfs_or_os_success (booleans/strings).

def extract(trial):
    title = trial.get("title", "")
    return {
        "phase": "3",
        "is_rct": "RCT" in title,
        "has_comparator": "RCT" in title,  # pretend RCT implies comparator here
        "pfs_or_os_success": "superiority" in title.lower(),
        # add registration fields later if C2 is implemented
    }