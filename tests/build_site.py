import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_site():
    subprocess.run(
        ["bundle", "exec", "jekyll", "build"],
        cwd=ROOT,
        check=True,
    )
