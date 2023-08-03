# CIMP-L > Data
#
#

import streamlit as st
import pandas as pd
import numpy as np

#--- DATA ---#
df_permittees = pd.read_excel(
    io='data.xlsx',
    engine='openpyxl',
    sheet_name='Permittees'
)
df_programs = pd.read_excel(
    io='data.xlsx',
    engine='openpyxl',
    sheet_name='Programs'
)

#--- CONTENT ---#
st.markdown("# Data")
st.dataframe(df_permittees)
st.dataframe(df_programs)

#--- SIDEBAR ---#
st.sidebar.markdown("""
    # Filter by...     
                    """)
st.sidebar.multiselect(
    "Permittee:",
    options=df_permittees["Permittee"].unique()
)
st.sidebar.multiselect(
    "Program:",
    options=df_programs["Program"].unique()
)

#
#
# CIMP-L > Data