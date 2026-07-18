import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_amr_explainer():
    path = BASE_DIR / "data" / "amr_explainer.md"
    return path.read_text(encoding="utf-8")

def load_disclaimer():
    path = BASE_DIR / "docs" / "disclaimer.md"
    return path.read_text(encoding="utf-8")

def load_myths_facts():
    path = BASE_DIR / "data" / "myths_facts.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_risk_questions():
    path = BASE_DIR / "data" / "risk_questions.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)