# Ransomware Simulator (Safe & Educational)

A Streamlit app that demonstrates ransomware behavior purely for awareness and training. This simulator does not read, modify, or exfiltrate any data. It renders a UI-only scenario to discuss detection and response.

## Features

- Global trends chart (demo data)
- Safe attack simulation with progress and response options
- Mitigation guide with best practices
- Phishing detection quiz
- Summary report

## Safety Guarantees

- No file system operations
- No process manipulation or persistence
- No network calls to external services (aside from loading an illustrative image)
- UI-only demonstration intended for training

## Quickstart

```bash
# 1) Create and activate a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Run the app
streamlit run app.py
```

Then open the URL shown in the terminal (typically <http://localhost:8501>).

## Notes

- Tested with Python 3.10+.
- If the image under Mitigation Guide doesn't load due to network policies, the app will still work.
- For workshops, consider projecting the simulator and discussing each step and recommended responses.

## License

Educational use only. Do not use this project to produce or distribute malware. The authors are not responsible for misuse.
