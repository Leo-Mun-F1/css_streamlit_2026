import streamlit as st

# GitHub raw PDF URL
pdf_url = "https://github.com/Leo-Mun-F1/css_streamlit_2026/blob/main/NITheCS%20Certif%202026.pdf"


st.markdown(f'<embed src="{pdf_url}" width="700" height="1000" type="application/pdf">', unsafe_allow_html=True)