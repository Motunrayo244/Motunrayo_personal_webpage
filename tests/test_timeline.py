import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import build_site

ROOT = Path(__file__).resolve().parents[1]
WHEN = [
    "November 2025–present",
    "3 November 2026",
    "June 2026",
    "May 2025–November 2025",
    "10–12 September 2025",
    "10 September 2025",
    "August 2023–July 2025",
    "17–20 June 2025",
    "September 2024–April 2025",
    "September 2024–December 2024",
    "June 2024–September 2024",
    "March 2024–August 2024",
    "May 2022–August 2023",
    "September 2020–April 2022",
    "2020",
    "April 2019–February 2020",
    "March 2014–October 2018",
    "April 2017–October 2017",
]


class WhenParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.values = []

    def handle_starttag(self, tag, attrs):
        if tag in ("li", "article"):
            found = dict(attrs).get("data-when")
            if found:
                self.values.append(found)


class TimelineTest(unittest.TestCase):
    def test_order_links_and_wolt_sentences(self):
        build_site()
        html = (ROOT / "_site" / "timeline" / "index.html").read_text()
        parser = WhenParser()
        parser.feed(html)
        self.assertEqual(parser.values, WHEN)
        self.assertIn("Detects the language of support messages.", html)
        self.assertIn("Assesses and coaches support agents.", html)
        self.assertIn("/Motunrayo_personal_webpage/projects/gearbox-sound/", html)
        self.assertIn("https://scholar.google.com/scholar?hl=sv&as_sdt=0%2C5&q=Motunrayo+ibiyo&oq=mo", html)
        self.assertNotIn("Snowflake", html)
        self.assertNotIn("Flyte", html)


if __name__ == "__main__":
    unittest.main()
