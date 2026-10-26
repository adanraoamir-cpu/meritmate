

import streamlit as st

st.set_page_config(
    page_title="MeritMate | University Admissions",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1020, #151e38);
    color: #f4f6ff;
}
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
h1, h2, h3, p, label {
    color: #f4f6ff !important;
}
div[data-testid="stMetric"] {
    background: #202b49;
    border: 1px solid #354365;
    padding: 18px;
    border-radius: 16px;
}
div.stButton > button {
    background: #6478ff;
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem 1rem;
    font-weight: 600;
}
div.stButton > button:hover {
    background: #8392ff;
    color: white;
}
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #18233e;
    border: 1px solid #344263;
    border-radius: 16px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("## 🎓 MeritMate")
st.caption("YOUR UNIVERSITY ADMISSION COMPANION")

st.markdown(
    "<h1 style='font-size:42px;'>Find your university.<br>"
    "<span style='color:#8c9aff;'>Know your merit.</span></h1>",
    unsafe_allow_html=True
)

st.write(
    "Calculate your aggregate, explore top universities, "
    "and plan your next chapter with confidence."
)

st.divider()

st.subheader("Explore top universities")

col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.markdown("### 🔷 FAST-NUCES")
        st.write("Computing, AI, Data Science and business.")
        if st.button("Explore FAST", use_container_width=True):
            st.session_state["university"] = "FAST-NUCES"

    with st.container(border=True):
        st.markdown("### 🟣 NUST")
        st.write("Computing, engineering and multiple disciplines.")
        if st.button("Explore NUST", use_container_width=True):
            st.session_state["university"] = "NUST"

with col2:
    with st.container(border=True):
        st.markdown("### 🟦 UET Lahore")
        st.write("Engineering, computing and technology.")
        if st.button("Explore UET Lahore", use_container_width=True):
            st.session_state["university"] = "UET Lahore"

    with st.container(border=True):
        st.markdown("### 🟪 GIKI")
        st.write("Engineering, computing and sciences.")
        if st.button("Explore GIKI", use_container_width=True):
            st.session_state["university"] = "GIKI"

st.divider()

st.header("📊 Calculate your aggregate")

university = st.selectbox(
    "Select university",
    ["NUST", "FAST-NUCES", "UET Lahore", "GIKI"],
    key="university"
)

st.info(
    "Enter your marks below. This preview uses a sample formula; "
    "official university-specific formulas are not enabled yet."
)

a, b = st.columns(2)

with a:
    matric = st.number_input(
        "Matric marks obtained", min_value=0,
        max_value=1200, value=0
    )
    matric_total = st.number_input(
        "Matric total marks", min_value=1,
        max_value=1200, value=1200
    )
    inter = st.number_input(
        "Intermediate marks obtained", min_value=0,
        max_value=1200, value=0
    )

with b:
    inter_total = st.number_input(
        "Intermediate total marks", min_value=1,
        max_value=1200, value=1200
    )
    test = st.number_input(
        "Entry test marks", min_value=0,
        max_value=200, value=0
    )
    test_total = st.number_input(
        "Entry test total marks", min_value=1,
        max_value=200, value=200
    )

if st.button("✨ Calculate My Merit", use_container_width=True):
    if matric > matric_total or inter > inter_total or test > test_total:
        st.error("Obtained marks cannot exceed total marks.")
    else:
        mp = matric / matric_total * 100
        ip = inter / inter_total * 100
        tp = test / test_total * 100

        aggregate = mp * 0.10 + ip * 0.40 + tp * 0.50

        st.success(f"Your sample aggregate is {aggregate:.2f}%")
        st.caption(
            "Sample weighting only — not an official "
            "aggregate for " + university + "."
        )

st.divider()
st.caption("Made by Adan · MeritMate")
