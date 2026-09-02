import streamlit as st
from fetch_data import get_differentials

st.title("FPL Differential Finder")

st.write("Find undervalued, low-ownership FPL players based on points-per-million.")

# a slider the user can drag - this replaces hardcoding max_ownership in the function call
max_ownership = st.slider("Maximum ownership %", min_value=1, max_value=30, value=10)

# call our function with whatever the slider is currently set to
results = get_differentials(max_ownership=max_ownership)

st.write(f"Found {len(results)} players under {max_ownership}% ownership")

# st.table / st.dataframe can display a list of dictionaries directly as a table
st.dataframe(results)