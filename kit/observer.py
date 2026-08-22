#!/usr/bin/env python3
"""Read-only heuristic observer for pending markers."""
import json, sys
from pathlib import Path

MARKERS = ("TODO", "FIXME", "PENDING", "blocked", "en attente")

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: observer.py DIRECTORY")
    root = Path(sys.argv[1])
    hits = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and path.suffix.lower() in {".md", ".toml", ".txt"}:
            for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
                if any(marker.lower() in line.lower() for marker in MARKERS):
                    hits.append({"source": str(path), "line": number, "signal": line.strip()[:180]})
    output = root / "observations.json"
    output.write_text(json.dumps({"schema_version": 1, "confidence": "heuristic", "signals": hits}, indent=2) + "\n", encoding="utf-8")
    print(output)

if __name__ == "__main__":
    main()

