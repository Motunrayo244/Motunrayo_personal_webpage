import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data"

TIMELINE_WHEN = [
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

SLUGS = [
    "malicious-pypi",
    "quality-by-prompt",
    "llm-multi-agent-systems",
    "water-network",
    "gearbox-sound",
    "carla-autonomy",
    "website-usability",
]


class DataTest(unittest.TestCase):
    def test_profile_and_forbidden_contact(self):
        text = (DATA / "profile.yml").read_text()
        self.assertIn("Motunrayo Ibiyo", text)
        self.assertIn("Applied Scientist · Espoo, Finland", text)
        self.assertIn("hiking · swimming · reading · gym", text)
        self.assertIn("https://www.linkedin.com/in/motunrayoibiyo/", text)
        self.assertNotIn("ibiyo" + "motunrayo@gmail.com", text)
        self.assertNotIn("+358 46 " + "541 5825", text)

    def test_projects_slugs_and_gearbox_link(self):
        text = (DATA / "projects.yml").read_text()
        for slug in SLUGS:
            self.assertIn(slug, text)
        self.assertIn("https://ieeexplore.ieee.org/abstract/document/11205565", text)
        self.assertIn("95% balanced accuracy", text)

    def test_timeline_order(self):
        lines = (DATA / "timeline.yml").read_text().splitlines()
        whens = [line.split("when: ", 1)[1].strip().strip('"') for line in lines if line.strip().startswith("when:")]
        self.assertEqual(whens, TIMELINE_WHEN)

    def test_blog_order(self):
        lines = (DATA / "blog.yml").read_text().splitlines()
        titles = [line.split("title: ", 1)[1].strip().strip('"') for line in lines if line.strip().startswith("title:")]
        self.assertEqual(
            titles,
            [
                "From Nigeria to Europe: An Erasmus Mundus Scholar’s Journey in EDISS",
                "Web scraping on your Computer",
                "Tales of an ML Engineer Wannabe: Network Analysis",
                "Data Engineering Zoomcamp Notebook",
            ],
        )


if __name__ == "__main__":
    unittest.main()
