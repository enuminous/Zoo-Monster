#!/usr/bin/env python3
"""MONSTER report gate checker and simple performance-envelope helper."""
import json, sys
from pathlib import Path


def within(value, direction, tolerance):
    if value is None: return False
    if direction == "higher_is_better": return value >= tolerance
    if direction == "lower_is_better": return value <= tolerance
    return isinstance(tolerance, (list, tuple)) and len(tolerance) == 2 and tolerance[0] <= value <= tolerance[1]


def envelope(values):
    xs=[v for v in values if isinstance(v,(int,float))]
    if not xs: return {"worst":None,"best":None,"mean":None}
    return {"worst":min(xs),"best":max(xs),"mean":sum(xs)/len(xs)}


def decide(report):
    prereg=report.get("preregistration", {})
    metric=report.get("metric", {})
    baseline=report.get("baseline", {})
    conditions=report.get("conditions", [])
    tol=metric.get("tolerance")
    if not prereg.get("registered_before_outcomes") or not prereg.get("protocol_id") or tol is None or not baseline.get("matched") or not conditions:
        return "N/A"
    mandatory=[c for c in conditions if c.get("registered")]
    if not mandatory: return "N/A"
    direction=metric.get("direction")
    # A demonstrated violation remains a failure even when another cell is missing.
    if any(c.get("status") == "complete" and c.get("candidate") is not None and not within(c.get("candidate"),direction,tol) for c in mandatory):
        return "FAIL"
    boundaries=report.get("failure_boundaries", [])
    if any(b.get("status") == "failure_observed" for b in boundaries): return "FAIL"
    if any(c.get("status") != "complete" or c.get("candidate") is None or c.get("baseline") is None for c in mandatory):
        return "N/A"
    if any(b.get("status") == "unknown" for b in boundaries): return "N/A"
    return "PASS"


def main():
    if len(sys.argv)!=2:
        print("Usage: python src/monster.py REPORT.json",file=sys.stderr); return 2
    report=json.loads(Path(sys.argv[1]).read_text())
    if report.get("animal")!="MONSTER":
        print("ERROR: animal must be MONSTER",file=sys.stderr); return 2
    actual=decide(report); declared=report.get("decision")
    print(f"declared={declared} computed={actual}")
    if actual!=declared:
        print("GATE MISMATCH",file=sys.stderr); return 1
    return 0

if __name__=="__main__": raise SystemExit(main())
