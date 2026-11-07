import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import build_site

ROOT = Path(__file__).resolve().parents[1]


class ScaffoldTest(unittest.TestCase):
    def test_build_writes_home_and_baseurl(self):
        build_site()
        html = (ROOT / "_site" / "index.html").read_text()
        config = (ROOT / "_config.yml").read_text()
        self.assertIn("/Motunrayo_personal_webpage", config)
        self.assertIn("<html", html)


if __name__ == "__main__":
    unittest.main()
