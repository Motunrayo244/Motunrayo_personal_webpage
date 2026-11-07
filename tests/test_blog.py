import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import build_site

ROOT = Path(__file__).resolve().parents[1]


class BlogTest(unittest.TestCase):
    def test_video_then_articles(self):
        build_site()
        html = (ROOT / "_site" / "blog" / "index.html").read_text()
        titles = [
            "From Nigeria to Europe: An Erasmus Mundus Scholar’s Journey in EDISS",
            "Web scraping on your Computer",
            "Tales of an ML Engineer Wannabe: Network Analysis",
            "Data Engineering Zoomcamp Notebook",
        ]
        positions = [html.index(title) for title in titles]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("https://www.master-ediss.eu/from-nigeria-to-europe-an-erasmus-mundus-scholars-journey-in-ediss/", html)
        self.assertIn("https://www.youtube.com/watch?v=Q4nkyC-BZ1o", html)
        self.assertIn("https://www.linkedin.com/in/motunrayoibiyo/recent-activity/articles/", html)
        self.assertIn("https://www.linkedin.com/pulse/data-engineering-zoomcamp-notebook-motunrayo-ibiyo", html)
        self.assertEqual(html.count("<iframe"), 0)


if __name__ == "__main__":
    unittest.main()
