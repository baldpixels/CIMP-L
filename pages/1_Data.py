# CIMP-L > Data

# load dependencies
import streamlit as st
import pandas as pd
import numpy as np

# load excel data
xl_permittees = pd.read_excel(
    io='data.xlsx',
    engine='openpyxl',
    sheet_name='Permittees'
)
xl_programs = pd.read_excel(
    io='data.xlsx',
    engine='openpyxl',
    sheet_name='Programs'
)

# load sidebar
st.sidebar.markdown("""
    # Filter by...     
                    """)
permittee = st.sidebar.multiselect(
    "Permittee:",
    options=xl_permittees["Permittee"].unique()
)
program = st.sidebar.multiselect(
    "Program:",
    options=xl_programs["Program"].unique()
)

#load markdown
st.markdown("# Data")