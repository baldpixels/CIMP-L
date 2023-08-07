# CIMP-L > Import Data

# load dependencies
import streamlit as st
import pandas as pd
import numpy as np
import tabula

# functions
def extract_data(file):
    tables = tabula.read_pdf(file, pages='all', multiple_tables=True)
    return tables

# load sidebar
st.sidebar.markdown("""
                    
    # CIMP-L
                    
    ## Monitoring data made *simple.*
                    
    """
    )

# load markdown
st.markdown("""
            
            # Import Data
            Use this tool to extract data tables from PDF monitoring reports.
            
            """)

# extract data tables from .pdf and display as panda dataframe
uploaded_file = st.file_uploader('Upload a .pdf here', type="pdf")
if uploaded_file is not None:
    pdf_tables = extract_data(uploaded_file)
    for df in pdf_tables:
        st.dataframe(df)