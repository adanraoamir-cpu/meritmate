

import streamlit as st

st.set_page_config(
    page_title="MeritMate",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 MeritMate")
st.subheader("Your University Merit Calculator")
st.write("Plan your university admission journey.")

st.divider()

st.header("📊 Calculate Your Aggregate")

st.write("Enter your marks below.")

matric = st.number_input(
    "Matric marks obtained",
    min_value=0,
    max_value=1200,
    value=0
)

matric_total = st.number_input(
    "Matric total marks",
    min_value=1,
    max_value=1200,
    value=1200
)

inter = st.number_input(
    "Intermediate marks obtained",
    min_value=0,
    max_value=1200,
    value=0
)

inter_total = st.number_input(
    "Intermediate total marks",
    min_value=1,
    max_value=1200,
    value=1200
)

test = st.number_input(
    "Entry test marks",
    min_value=0,
    max_value=200,
    value=0
)

test_total = st.number_input(
    "Entry test total marks",
    min_value=1,
    max_value=200,
    value=200
)

if st.button("Calculate My Aggregate"):
    if matric > matric_total or inter > inter_total:
        st.error("Obtained marks cannot exceed total marks.")
    elif test > test_total:
        st.error("Entry test marks cannot exceed total marks.")
    else:
        matric_pct = matric / matric_total * 100
        inter_pct = inter / inter_total * 100
        test_pct = test / test_total * 100

        aggregate = (
            matric_pct * 0.10
            + inter_pct * 0.40
            + test_pct * 0.50
        )

        st.success(
            f"Your sample aggregate is {aggregate:.2f}%"
        )
        st.caption(
            "Sample formula only: confirm the official "
            "weightage for your chosen university."
        )

st.divider()
st.caption("Made by Adan | MeritMate")
