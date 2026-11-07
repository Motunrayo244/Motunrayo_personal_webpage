import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import build_site

ROOT = Path(__file__).resolve().parents[1]


class FrameTest(unittest.TestCase):
    def test_nav_palettes_and_boot_script(self):
        build_site()
        html = (ROOT / "_site" / "index.html").read_text()
        css = (ROOT / "assets" / "css" / "site.css").read_text()
        self.assertIn("https://www.linkedin.com/in/motunrayoibiyo/", html)
        self.assertIn("https://github.com/Motunrayo244", html)
        self.assertIn('src="/Motunrayo_personal_webpage/assets/js/site.js"', html)
        self.assertIn("Let’s connect", html)
        self.assertNotIn("theme.js", html)
        self.assertIn("#f5f6fa", css)
        self.assertIn("#4359bd", css)
        self.assertIn("Playfair Display", css)
        self.assertIn("max-width:600px", css)
        self.assertNotIn("<form", html)


if __name__ == "__main__":
    unittest.main()
