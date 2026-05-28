
import streamlit as st

from config import APP_TITLE, PAGE_ICON

st.set_page_config(
page_title=APP_TITLE,
page_icon=PAGE_ICON,
layout="wide"
)

st.title("🤎 Business Location DSS")

st.success("🚀 Deployment Successful")

st.write("""
Sistem Pendukung Keputusan
untuk menentukan lokasi usaha terbaik
menggunakan berbagai metode DSS.
""")

st.info("""
Menu DSS:

* Dashboard
* Data Driven DSS
* EV & EOL
* Monte Carlo
* Utility Function
* Recommendation Engine
  """)
  