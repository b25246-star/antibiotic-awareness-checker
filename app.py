import streamlit as st
from modules.content import load_amr_explainer, load_disclaimer, load_myths_facts, load_risk_questions
from modules.risk_engine import calculate_risk

st.set_page_config(
    page_title="Antibiotic Misuse Awareness Checker",
    page_icon="⚕️",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    .main {
        padding-top: 0.5rem;
    }
    h1, h2, h3 {
        font-weight: 600 !important;
        letter-spacing: -0.01em;
    }
    p, li, label {
        line-height: 1.55;
    }
    .stRadio > label {
        font-weight: 500;
        font-size: 0.98rem;
        color: #C4CCD6;
    }
    div[data-testid="stForm"] {
        background-color: #161B23 !important;
        padding: 1.75rem 1.75rem 1.25rem 1.75rem !important;
        border-radius: 6px !important;
        border: 1px solid #262D38 !important;
    }
    div[data-testid="stExpander"] {
        border-radius: 6px !important;
        border: 1px solid #262D38 !important;
        background-color: #12161D !important;
    }

    /* Professional flat button */
    button[kind="formSubmit"],
    button[kind="secondaryFormSubmit"],
    .stButton button {
        background-color: transparent !important;
        color: #5B8DEF !important;
        font-weight: 600 !important;
        border-radius: 4px !important;
        padding: 0.55rem 1.6rem !important;
        border: 1px solid #5B8DEF !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.03em;
        text-transform: uppercase;
        transition: all 0.15s ease;
    }
    button[kind="formSubmit"]:hover,
    button[kind="secondaryFormSubmit"]:hover,
    .stButton button:hover {
        background-color: #5B8DEF !important;
        color: #0F1419 !important;
        border: 1px solid #5B8DEF !important;
    }

    .section-label {
        text-transform: uppercase;
        font-size: 0.72rem;
        letter-spacing: 0.08em;
        color: #6B7684;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    hr {
        border-color: #262D38 !important;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #10141B;
        border-right: 1px solid #262D38;
    }
    section[data-testid="stSidebar"] .stRadio > label {
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar Navigation ----------
with st.sidebar:
    st.markdown("""
    <div style="padding: 0.5rem 0 1rem 0;">
        <div class="section-label">Public Health Tool</div>
        <h2 style="margin:0; color:#EDEFF2; font-size:1.3rem;">AMR Awareness</h2>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigate",
        ["Home", "Risk Checker", "Myth vs Fact"],
        label_visibility="collapsed"
    )

    st.markdown("<div style='margin-top:2rem;'></div>", unsafe_allow_html=True)
    st.caption("Educational tool. Not a diagnostic device. Always consult a doctor or pharmacist.")


# =========================================================
# PAGE: HOME
# =========================================================
if page == "Home":
    st.markdown("""
    <div style="padding: 2rem 0 1.75rem 0;">
        <div class="section-label">Public Health · Awareness Tool</div>
        <h1 style="margin:0; color:#EDEFF2; font-size:2.3rem;">Antibiotic Misuse Awareness &amp; Risk Checker</h1>
        <p style="margin-top:0.8rem; color:#8B94A3; font-size:1.05rem; max-width: 640px;">
            A brief, honest self-assessment to help you recognize common antibiotic misuse patterns
            and understand their role in antimicrobial resistance (AMR).
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.warning(load_disclaimer())

    st.divider()

    with st.expander("What is Antimicrobial Resistance (AMR)?"):
        st.markdown(load_amr_explainer())

    st.divider()

    st.markdown('<div class="section-label">Get Started</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div style="border:1px solid #262D38; border-radius:6px; padding:1.25rem; background-color:#12161D; height:100%;">
            <h3 style="margin:0; font-size:1.05rem; color:#EDEFF2;">Risk Checker</h3>
            <p style="color:#8B94A3; font-size:0.9rem; margin-top:0.5rem;">
                Answer six short questions about your antibiotic habits and get an honest, transparent risk result.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="border:1px solid #262D38; border-radius:6px; padding:1.25rem; background-color:#12161D; height:100%;">
            <h3 style="margin:0; font-size:1.05rem; color:#EDEFF2;">Myth vs Fact</h3>
            <p style="color:#8B94A3; font-size:0.9rem; margin-top:0.5rem;">
                Common misconceptions about antibiotics, corrected with guidance from WHO, CDC, and ICMR.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.caption("Use the sidebar to navigate to either section.")


# =========================================================
# PAGE: RISK CHECKER
# =========================================================
elif page == "Risk Checker":
    st.markdown('<div class="section-label">Self-Assessment</div>', unsafe_allow_html=True)
    st.subheader("Risk Check")
    st.write("Answer honestly. This is a private, awareness-only self-check — nothing is stored or shared.")

    questions = load_risk_questions()
    answers = {}

    with st.form("risk_quiz_form"):
        for q in questions:
            answers[q["id"]] = st.radio(q["question"], q["options"], key=q["id"])
        submitted = st.form_submit_button("Check My Risk")

    if submitted:
        total, max_score, risk_level, flags = calculate_risk(answers, questions)

        st.markdown('<div class="section-label">Result</div>', unsafe_allow_html=True)

        risk_colors = {
            "Low Risk":      ("#12261F", "#4ADE80"),
            "Moderate Risk": ("#2A2312", "#F5B840"),
            "High Risk":     ("#2A1414", "#F0685C"),
        }
        bg, accent = risk_colors[risk_level]

        st.markdown(f"""
        <div style="background-color:{bg}; border: 1px solid {accent}40; padding: 1.25rem 1.5rem; border-radius: 6px; margin: 0.5rem 0 1rem 0;">
            <h3 style="margin:0; color:{accent}; font-size:1.2rem;">{risk_level}</h3>
            <p style="margin-top:0.4rem; margin-bottom:0; color:#C4CCD6; font-size:0.9rem;">
                Score: {total} / {max_score}
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.progress(min(total / max_score, 1.0))

        if flags:
            st.markdown("**Habits flagged for awareness:**")
            for f in flags:
                st.markdown(f"- {f}")
        else:
            st.markdown("No risky habits flagged based on your answers.")

        st.info("This is not a medical diagnosis. Please consult a doctor or pharmacist for guidance specific to your health.")

    st.divider()
    st.caption("This tool provides general awareness content only and does not replace professional medical advice.")


# =========================================================
# PAGE: MYTH VS FACT
# =========================================================
elif page == "Myth vs Fact":
    st.markdown('<div class="section-label">Education</div>', unsafe_allow_html=True)
    st.subheader("Myth vs Fact")
    st.write("Common misconceptions about antibiotics, corrected using WHO, CDC, and ICMR guidance.")

    myths_facts = load_myths_facts()

    for item in myths_facts:
        with st.expander(f"Myth: {item['myth']}"):
            st.markdown(f"**Fact:** {item['fact']}")

    st.divider()