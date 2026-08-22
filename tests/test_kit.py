import json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]

class KitTests(unittest.TestCase):
    def test_registry_and_context(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "registry.toml"
            source.write_text((ROOT / "examples/minimal/registry.toml").read_text(), encoding="utf-8")
            subprocess.run([sys.executable, str(ROOT / "kit/registry.py"), str(source)], check=True)
            result = subprocess.run([sys.executable, str(ROOT / "kit/render_context.py"), str(source.with_suffix(".json"))], check=True, capture_output=True, text=True)
            self.assertIn("CT-2026-014", result.stdout)
            self.assertEqual(json.loads(source.with_suffix(".json").read_text())["schema_version"], 1)

if __name__ == "__main__":
    unittest.main()

