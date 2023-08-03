# CIMP-L > Permittees

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

# load sidebar
st.sidebar.markdown("""
                    
    # CIMP-L
                    
    Monitoring data made *simple.*
                    
    """
    )

# load markdown
st.markdown("# Permittees")