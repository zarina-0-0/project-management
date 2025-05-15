import streamlit as st

# --- PAGE SETUP ---
main_page = st.Page(
    page="pages/maininfo.py",
    title="красИИвее",
    icon=":material/home:",
    default=True
)

about_page = st.Page(
    page="pages/about_us.py",
    title="наша миссия",
    icon=":material/account_circle:",
)

page = st.Page(
    page="pages/4th.py",
    title="иср",
    icon=":material/loyalty:"
)

tables_page = st.Page(
    page="pages/accountings.py",
    title="бизнес модель",
    icon=":material/bar_chart:",
)

nav = st.navigation(pages=[main_page, about_page, tables_page, page])
nav.run()
