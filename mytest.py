%%writefile mytest.py
import streamlit as st
import numpy as np
import pandas as pd

st.header("mytest App")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.write('You selected:', option)
