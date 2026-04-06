import streamlit as st
import matplotlib.pyplot as plt
from model import analyze_complexity
from utils import clean_code

st.set_page_config(
    page_title="Code Complexity Analyzer Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------- Custom CSS -----------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(90deg,#1f4037,#99f2c8);
    padding: 30px;
    border-radius: 15px;
    text-align:center;
    color:white;
    margin-bottom:25px;
}
.card {
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 6px 18px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ----------------- Hero Section -----------------
st.markdown("""
<div class="hero">
<h1>📊 Code Complexity Analyzer Pro</h1>
<p>Professional Static Code Analysis Dashboard</p>
</div>
""", unsafe_allow_html=True)

# ----------------- Sidebar -----------------
st.sidebar.title("⚙️ Analysis Options")

analysis_type = st.sidebar.multiselect(
    "Select Metrics",
    ["Basic Metrics", "Time Complexity", "Cyclomatic Complexity", "Nested Depth"],
    default=["Basic Metrics", "Time Complexity"]
)

uploaded_file = st.sidebar.file_uploader("Upload Python File", type=["py"])

manual_code = st.sidebar.checkbox("Or Paste Code Manually")

if manual_code:
    code_input = st.text_area("Paste Code Here", height=300)
elif uploaded_file:
    code_input = uploaded_file.read().decode("utf-8")
else:
    code_input = ""

analyze_button = st.sidebar.button("🚀 Run Analysis")

# ----------------- Main Panel -----------------
if analyze_button and code_input.strip() != "":

    cleaned_code = clean_code(code_input)
    results = analyze_complexity(cleaned_code)

    st.subheader("📌 Code Preview")
    st.code(cleaned_code, language="python")

    st.subheader("📈 Analysis Results")

    col1, col2, col3 = st.columns(3)

    if "Basic Metrics" in analysis_type:
        with col1:
            st.metric("Lines of Code", results["lines"])
            st.metric("Functions", results["functions"])

        with col2:
            st.metric("Loops", results["loops"])
            st.metric("Conditions", results["conditions"])

    if "Time Complexity" in analysis_type:
        with col3:
            st.metric("Estimated Time Complexity", results["complexity"])

    if "Cyclomatic Complexity" in analysis_type:
        st.info(f"Cyclomatic Complexity: {results['cyclomatic']}")

    if "Nested Depth" in analysis_type:
        st.info(f"Max Nested Loop Depth: {results['nested_depth']}")

    # ----------------- Chart -----------------
    st.subheader("📊 Visualization")

    metrics = [
        results["lines"],
        results["functions"],
        results["loops"],
        results["conditions"]
    ]

    labels = ["Lines", "Functions", "Loops", "Conditions"]

    fig = plt.figure()
    plt.bar(labels, metrics)
    plt.title("Code Metrics Overview")
    st.pyplot(fig)

    # ----------------- Download Report -----------------
    report = f"""
    CODE COMPLEXITY REPORT

    Lines: {results['lines']}
    Functions: {results['functions']}
    Loops: {results['loops']}
    Conditions: {results['conditions']}
    Estimated Time Complexity: {results['complexity']}
    Cyclomatic Complexity: {results['cyclomatic']}
    Nested Loop Depth: {results['nested_depth']}
    """

    st.download_button(
        "📥 Download Report",
        report,
        file_name="complexity_report.txt"
    )

elif analyze_button:
    st.warning("Please provide code before running analysis.")