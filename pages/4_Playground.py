# Playground
#
#

import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.text_input("Your name", key="name")

if len(st.session_state.name) != 0:
    st.sidebar.write("Hello " + st.session_state.name + ".")

add_selectbox = st.sidebar.selectbox(
    'Select an element to display',
    ('Data Table', 'Line Chart', 'Map'))

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))

if add_selectbox == 'Data Table':
    df = pd.DataFrame(
        np.random.randn(10, 20),
        columns=('col %d' % i for i in range(20)))
    st.table(df)

if add_selectbox == 'Line Chart':
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns = ['a','b','c'])
    st.line_chart(chart_data)

if add_selectbox == 'Map':
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_data)

#
#
# Playground
