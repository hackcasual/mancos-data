#!/usr/bin/env python3
"""Builds bundles/manifest.json from the .yafcbundle files present.

Same manifest shape the Mancos app consumes:
  {"packs": [{"id", "name", "file", "bytes"}]}
"""
import json
import os
import sys

bundle_dir = sys.argv[1] if len(sys.argv) > 1 else "bundles"
packs = []
for name in sorted(os.listdir(bundle_dir)):
    if not name.endswith(".yafcbundle"):
        continue
    stem = name[: -len(".yafcbundle")]
    packs.append({
        "id": stem,
        "name": stem.replace("-", " ").replace("_", " ").title(),
        "file": "bundles/" + name,
        "bytes": os.path.getsize(os.path.join(bundle_dir, name)),
    })
with open(os.path.join(bundle_dir, "manifest.json"), "w") as f:
    json.dump({"packs": packs}, f, indent=1)
print(f"manifest: {len(packs)} pack(s)")
