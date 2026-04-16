#!/usr/bin/env python3
import os
import platform
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> None:
    print(">", " ".join(cmd))
    subprocess.run(cmd, check=True)


def main() -> int:
    project_dir = Path(__file__).resolve().parent
    venv_dir = project_dir / ".venv"

    if not venv_dir.exists():
        print("Creating virtual environment...")
        run([sys.executable, "-m", "venv", str(venv_dir)])
    else:
        print("Virtual environment already exists.")

    if platform.system().lower().startswith("win"):
        py = venv_dir / "Scripts" / "python.exe"
    else:
        py = venv_dir / "bin" / "python"

    print("Installing dependencies...")
    run([str(py), "-m", "pip", "install", "--upgrade", "pip"])
    run([str(py), "-m", "pip", "install", "-r", str(project_dir / "requirements.txt")])

    print("\nSetup complete.")
    if platform.system().lower().startswith("win"):
        print(r"Activate venv: .\.venv\Scripts\activate")
    else:
        print("Activate venv: source .venv/bin/activate")
    print("Run project: python main.py")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Setup failed with exit code {exc.returncode}")
        raise SystemExit(exc.returncode)
