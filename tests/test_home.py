import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import build_site

ROOT = Path(__file__).resolve().parents[1]
TITLES = [
    "Malicious PyPI package detection",
    "Quality by Prompt",
    "LLM-based multi-agent systems",
    "Water-network monitoring",
    "Gearbox sound anomaly detection",
    "Carla autonomy",
    "Website usability",
]


class HomeTest(unittest.TestCase):
    def test_home_order_and_seven_cards(self):
        build_site()
        page = (ROOT / "_site" / "index.html").read_text()
        html = page.split("<main", 1)[1]
        markers = [
            "Applied Scientist · Espoo, Finland",
            "Motunrayo.",
            "researching large language models, multi-agent systems, and data-intensive software.",
            "Malicious PyPI package detection",
            "Hiking",
        ]
        positions = [html.index(marker) for marker in markers]
        self.assertEqual(positions, sorted(positions))
        for title in TITLES:
            self.assertIn(title, html)
            self.assertIn("/Motunrayo_personal_webpage/projects/", html)
        self.assertEqual(html.count('class="project-card'), 7)
        self.assertIn('class="orbit-art"', html)
        self.assertIn("https://scholar.google.com/scholar?hl=sv&as_sdt=0%2C5&q=Motunrayo+ibiyo&oq=mo", page)
        self.assertIn("https://github.com/Motunrayo244", page)


if __name__ == "__main__":
    unittest.main()
