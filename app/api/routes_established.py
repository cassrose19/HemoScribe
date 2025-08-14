# API layer — lightweight HTTP endpoints (demo)
#
# What this file does:
#   • POST /established/scan: runs one scan and returns how many items queued.
#   • GET  /established/candidates: returns the in-memory review queue.
from fastapi import APIRouter
from app.pipeline.scan_established import scan_once, CANDIDATES
router = APIRouter()

router.post("/scan")

@router.post("/scan")
def scan(): return {"queued": scan_once()}

@router.get("/candidates")
def list_new(): return CANDIDATES
