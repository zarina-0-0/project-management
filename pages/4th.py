import streamlit as st


st.markdown("""
    <style>
        .center-title {
            text-align: center;
            font-size: 2em;
        }
        .pink-text {
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="center-title">
        <span class="pink-text">ИСР организованная по фазам
</span>
    </div>
""", unsafe_allow_html=True)

st.image("materials/6.png")
st.markdown("""
    <div class="center-title">
        <span class="pink-text">ИСР по функциям сервиса
</span>
    </div>
""", unsafe_allow_html=True)

st.image("materials/7.png")

st.markdown("""
    <div class="center-title">
        <span class="pink-text">матрица ответственности
</span>
    </div>
""", unsafe_allow_html=True)

st.image("materials/8.png")
