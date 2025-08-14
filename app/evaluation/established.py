# Rules engine — applies criteria C1/C3 (demo)
#
# What this file does:
#   • Computes whether a trial meets “established” based on simple features.
#   • Returns (ok, reasons[]) where reasons are human-readable strings.
#
# Criteria implemented:
#   • C1: comparator in phase 3 RCT
#   • C3: PFS/OS superiority or non-inferiority in phase 3
#   • (C2 can be added later for FDA/EMA regular approval.)

def decide(ex):
    c1 = ex["phase"] == "3" and ex["is_rct"] and ex["has_comparator"]
    c3 = ex["phase"] == "3" and ex["pfs_or_os_success"]
    ok, reasons = (c1 or c3), []
    if c1: reasons.append("C1: comparator in phase 3 RCT")
    if c3: reasons.append("C3: PFS/OS success in phase 3")
    return ok, reasons