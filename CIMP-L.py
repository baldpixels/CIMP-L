# CIMP-L

# load dependencies
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CIMP-L",
                   page_icon=":bar_chart:")

# load sidebar
st.sidebar.markdown("""
                    
    # CIMP-L
                    
    Monitoring data made *simple.*
                    
    """
    )

# load markdown
st.markdown(    
    """

    # What is CIMP-L?
    
    CIMP-L (which stands for "CIMP-Library") is a collaborative web dashboard for interacting with CIMP data using simple Excel spreadsheets as its back-end.

    """
    )