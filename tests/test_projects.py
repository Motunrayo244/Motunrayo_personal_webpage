import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_site import build_site

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "malicious-pypi": [
        "95% balanced accuracy",
        "https://github.com/Motunrayo244/Multi-agent-Malicious-Package-Detector-MA-MPD-",
        "https://github.com/Motunrayo244/MA-MPD-experiment-report",
        "https://doi.org/10.1145/3756681.3757042",
        "https://doi.org/10.1016/j.jss.2026.112792",
        "few-shot learning is more effective",
        "This paper presents LAMPS",
    ],
    "quality-by-prompt": [
        "Great Expectations",
        "https://github.com/Motunrayo244/ge-app",
        "https://doi.org/10.1007/978-3-032-04190-6_9",
        "LLaMA-3.2-3B-bnb-4bit",
    ],
    "llm-multi-agent-systems": [
        "3 November 2026",
        "https://link.springer.com/article/10.1007/s10664-026-10955-8",
        "Metagente software engineering scenario",
    ],
    "water-network": ["water distribution network", "https://github.com/Motunrayo244/SE4IoT_water_distribution_network"],
    "gearbox-sound": [
        "10 September 2025",
        "https://ieeexplore.ieee.org/abstract/document/11205565",
        "88% specificity",
    ],
    "carla-autonomy": [
        "Repository for Carla autonomy using MAPE-K.",
        "https://github.com/Motunrayo244/Carla-Autonomous-Using-Mape-k",
        "https://www.youtube.com/embed/cC3kg6nT_1A",
        "MAPE-K loop",
    ],
    "website-usability": ["Nigerian University Websites", "https://github.com/Motunrayo244/Website_Usability"],
}


class ProjectTest(unittest.TestCase):
    def test_each_project_page(self):
        build_site()
        for slug, needles in EXPECTED.items():
            html = (ROOT / "_site" / "projects" / slug / "index.html").read_text()
            for needle in needles:
                self.assertIn(needle, html)
        carla = (ROOT / "_site" / "projects" / "carla-autonomy" / "index.html").read_text()
        self.assertNotIn("algorithm", carla.lower())


if __name__ == "__main__":
    unittest.main()
