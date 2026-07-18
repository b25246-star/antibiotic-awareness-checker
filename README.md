# Antibiotic Misuse Awareness & Risk Checker

An AI-assisted public health awareness tool that helps people recognize risky antibiotic habits and understand antimicrobial resistance (AMR) — built for the *AI-Based Antibiotic Misuse Awareness & Risk Checker* challenge.

**This is an educational awareness tool only. It does not diagnose, does not recommend medication, and is not a substitute for professional medical advice.**

## What it does

- **Risk Checker** — a short, honest self-assessment (6 questions) that flags specific unsafe habits (self-medication, incomplete courses, viral misuse, sharing prescriptions) using transparent, rule-based scoring — no black-box logic.
- **AMR Explainer** — a plain-language explanation of what antimicrobial resistance is, why it happens, and why it matters, paraphrased from WHO / CDC / ICMR public guidance.
- **Myth vs Fact** — corrects common antibiotic misconceptions with sourced facts.
- **Real safety disclaimer** — shown prominently on load and repeated throughout, not just decorative.

## Tech stack

- **Streamlit** (Python) — UI and app logic
- Rule-based scoring engine (`modules/risk_engine.py`) — fully explainable, no ML/black-box model
- Content sourced from WHO, CDC, and ICMR public fact sheets, paraphrased for general awareness

## Project structure

```
├── app.py                  # Main Streamlit app
├── modules/
│   ├── risk_engine.py      # Transparent risk scoring logic
│   └── content.py          # Loads AMR explainer, myths/facts, quiz questions
├── data/
│   ├── risk_questions.json
│   ├── myths_facts.json
│   └── amr_explainer.md
├── docs/
│   └── disclaimer.md
└── .streamlit/
    └── config.toml         # App theme
```

## Running locally

```bash
python -m venv venv
venv\Scripts\Activate.ps1        # Windows PowerShell
pip install -r requirements.txt
python -m streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Deliverables

- Working prototype (this repo)
- 3–5 slide pitch deck (`AMR_Awareness_Pitch.pptx`)
- Standalone AMR explanation (`AMR_Explainer.pdf`)
- Safety disclaimer (in-app and in the PDF)

## Data sources

- [WHO Antimicrobial Resistance Fact Sheets](https://www.who.int/news-room/fact-sheets/detail/antimicrobial-resistance)
- CDC antibiotic use resources
- ICMR treatment guidelines

## Disclaimer

This tool is for general awareness and educational purposes only. It is not a medical device, does not diagnose any condition, and does not replace guidance from a qualified doctor or pharmacist. Always consult a healthcare professional before making decisions about antibiotic use.