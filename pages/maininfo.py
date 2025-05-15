import streamlit as st

st.markdown("""
    <style>
        .center-title {
            text-align: center;
            font-size: 5em;
        }
        .pink-text {
            color: #cc7390;
        }
    </style>
""", unsafe_allow_html=True)

col, coll, colll = st.columns(3)
coll.image("materials/pink.png")

st.markdown("""
    <div class="center-title">
        КРАС<span class="pink-text">ИИ</span>ВЕЕ
    </div>
""", unsafe_allow_html=True)


col_1, col_2, col_3 = st.columns([10,7,10])
col_2.markdown("""
    <div>
        <span class="pink-text">open your beauty with AI</span>
    </div>""", unsafe_allow_html=True)
co, column, c = st.columns([1,1,1])

with st.container(height=500):
    st.markdown("""
        <h3>
            крас<span class="pink-text">ИИ</span>вее
        – это не просто сервис, это ваш личный помощник в мире красоты и ухода</h3>
    """, unsafe_allow_html=True)
    st.markdown("""
    Мы предлагаем цифровой сервис для подбора косметики. 
    Вы можете загрузить фотографию с желаемым макияжем и снимок вашей кожи, а также указать данные о типе кожи, 
    наличии аллергий и предпочтениях по брендам. На основе этих данных система сформирует персонализированные рекомендации 
    по уходовой и декоративной косметике""")
    st.markdown("""
    <div>
        <b><span class="pink-text">Широкий выбор</span></b>
    </div>""", unsafe_allow_html=True)
    st.markdown("""Разнообразие экологичных косметических продуктов - от ухода до декоративной косметики 
    - чтобы каждый мог найти идеальные средства для себя""")
    st.markdown("""
        <div>
            <b><span class="pink-text">Универсальность</span></b>
        </div>""", unsafe_allow_html=True)
    st.markdown("""Учет индивидуальных особенностей кожи, аллергий и предпочтений, 
    обеспечивая персонализированные рекомендации для любого типа и стиля""")
    st.markdown("""
            <div>
                <b><span class="pink-text">С заботой о природе</span></b>
            </div>""", unsafe_allow_html=True)
    st.markdown("""Все рекомендуемые продукты созданы из натуральных и экологически чистых ингредиентов, 
                поддерживая здоровье вашей кожи и бережное отношение к окружающей среде""")

_1,_2,_3 = st.columns([1.85,2,0.9])
_3.link_button("contact us", "https://mail.google.com/mail/u/0/?pli=1#inbox",icon=":material/mail:")
_2.link_button("explore brands", "",icon=":material/shopping_cart:")
_1.link_button("try", "",icon=":material/loyalty:")