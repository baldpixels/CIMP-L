# CIMP-L
#
#

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CIMP-L",
                   page_icon=":bar_chart:")

#--- CONTENT ---#
st.markdown(    
    """

    # What is CIMP-L?
    
    CIMP-L (which stands for "CIMP-Library") is a collaborative web dashboard for interacting with CIMP data using simple Excel spreadsheets as its back-end.

    """
    )

#--- SIDEBAR ---#
st.sidebar.markdown("""
                    
    # CIMP-L
                    
    Monitoring data made *simple.*
                    
    """)

#
#
# CIMP-L