import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import build_site

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = [
    "ibiyo" + "motunrayo@gmail.com",
    "+358 46 " + "541 5825",
    "35846" + "5415825",
]


class AcceptanceTest(unittest.TestCase):
    def test_404_and_private_contact_absent(self):
        build_site()
        missing = (ROOT / "_site" / "404.html").read_text()
        self.assertIn("/Motunrayo_personal_webpage/timeline/", missing)
        self.assertIn("/Motunrayo_personal_webpage/blog/", missing)
        self.assertIn('href="/Motunrayo_personal_webpage/"', missing)
        built = ""
        for path in (ROOT / "_site").rglob("*.html"):
            built += path.read_text()
        for secret in FORBIDDEN:
            self.assertNotIn(secret, built)
        self.assertNotIn("<form", built)


if __name__ == "__main__":
    unittest.main()
