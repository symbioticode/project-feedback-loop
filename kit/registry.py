#!/usr/bin/env python3
"""Convert the small TOML registry into deterministic JSON."""
import json, sys, tomllib
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: registry.py REGISTRY.toml")
    source = Path(sys.argv[1])
    data = tomllib.loads(source.read_text(encoding="utf-8"))
    output = source.with_suffix(".json")
    output.write_text(json.dumps({"schema_version": 1, "items": data.get("item", [])}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)

if __name__ == "__main__":
    main()

