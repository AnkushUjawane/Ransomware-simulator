import streamlit as st
import time
import pandas as pd

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Ransomware Simulator", layout="wide")

# ---- DARK HACKER STYLE ----
st.markdown("""
<style>
body {
    background-color: #0a0f0a;
    color: #00ff9c;
}
div.stButton > button {
    background-color: black;
    color: #00ff9c;
    border-radius: 8px;
    border: 1px solid #00ff9c;
}
div.stButton > button:hover {
    background-color: #003300;
}
.sidebar .sidebar-content {
    background-color: #000;
}
</style>
""", unsafe_allow_html=True)

# ---- MENU ----
menu = ["Home", "Simulate Attack", "Mitigation Guide", "Phishing Quiz", "Report"]
choice = st.sidebar.radio("Navigation", menu)

# ---- HOME ----
if choice == "Home":
    st.title("💀 Ransomware Trends & Protection Simulator")
    st.write("A cybersecurity prototype demonstrating ransomware awareness and mitigation.")
    
    st.subheader("📈 Global Ransomware Trends")
    data = pd.DataFrame({
        "Year": [2021, 2022, 2023, 2024, 2025],
        "Attacks": [120, 240, 380, 450, 520]
    })

    st.line_chart(data.set_index("Year"))

    st.write("""
    **Key Insights**
    - Ransomware attacks increasing YoY
    - Rise of RaaS (Ransomware-as-a-Service)
    - Phishing & social engineering primary entry points
    """)

# ---- SIMULATE RANSOMWARE ----
elif choice == "Simulate Attack":
    st.title("⚠️ Ransomware Attack Simulation")
    st.write("This is a strictly educational and safe simulation of ransomware behavior. No files are touched, no processes are altered, and no network calls are made.")

    st.code(
        """
Safety guarantees (simulator):
- Does not read, modify, encrypt, or delete any files
- No background processes or persistence
- No network activity or data exfiltration
- UI-only demonstration for awareness training
""",
        language="text",
    )

    if st.button("Start Attack Simulation 🚨"):
        messages = [
            "Initializing payload...",
            "Scanning for target files...",
            "Encrypting files...",
            "Locking system directories...",
            "Disabling system restore...",
            "Dropping ransom note...",
            "Exfiltrating critical files...",
        ]

        status = st.empty()
        progress = st.progress(0)
        step_count = len(messages)
        for i, msg in enumerate(messages, start=1):
            status.write(msg)
            progress.progress(int(i * 100 / step_count))
            time.sleep(0.8)

        st.error("💀 Your files have been encrypted!")
        st.write("Pay 1 BTC to restore your data. 😈 (Don’t actually do this—see recommended responses below.)")

        st.subheader("Your Response:")
        col1, col2, col3 = st.columns(3)

        if col1.button("Disconnect Internet"):
            st.success("✅ Good job! You prevented further spread.")

        if col2.button("Restore Backup"):
            st.success("✅ Great! Recovery without paying ransom.")

        if col3.button("Pay Ransom"):
            st.warning("❌ Paying encourages cybercrime & may NOT recover files.")

# ---- MITIGATION ----
elif choice == "Mitigation Guide":
    st.title("🛡 Ransomware Mitigation Strategies")

    st.write("""
### ✅ Best Practices
- Regular encrypted backups
- Zero-Trust architecture
- MFA everywhere
- Network segmentation
- Real-time EDR tools
- Email phishing filters
- Employee training
""")

    st.image("https://i.imgur.com/E8nYhM2.png", caption="Zero-Trust Model", use_column_width=True)

# ---- PHISHING QUIZ ----
elif choice == "Phishing Quiz":
    st.title("🎯 Ransomware Phishing Detection Quiz")

    questions = [
        ("Your bank asks you to verify your password via email. Legit?", "No"),
        ("Unexpected invoice attachment from unknown sender?", "No"),
        ("Email domain looks suspicious (g00gle.com)?", "No"),
        ("Security update from Microsoft official site?", "Yes"),
    ]

    score = 0
    for q, correct in questions:
        ans = st.radio(q, ["Yes", "No"], key=q)
        if ans == correct:
            score += 1

    if st.button("Submit Quiz"):
        st.success(f"Your score: {score}/{len(questions)}")

# ---- REPORT ----
elif choice == "Report":
    st.title("📜 Prototype Summary Report")

    st.write("""
### System Purpose
Demonstrate ransomware behavior & educate users on response.

### Key Features
- Attack Simulation
- Trends Visualization
- Mitigation Guide
- Phishing Awareness Quiz

### Scope
**Educational prototype only — no real malware used.**
""")
