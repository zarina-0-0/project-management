import streamlit as st

col, coll, colll = st.columns([1,2,1])
col1, col2 = st.columns([10,10])

st.markdown("""
    <style>
        .title {
            font-size: 2em;
        }
        .pink-text {
            color: #cc7390;
        }
    </style>
""", unsafe_allow_html=True)

col2.markdown("""
    <div class="title">
        <span class="pink-text">проблемы</span>
    </div>
""", unsafe_allow_html=True)

col1.image("materials/4.png")
col1.image("materials/5.png")
col2.markdown("""
              Дорогостоящие консультации у профессиональных косметологов
              
              Сложно подобрать косметику, подходящую под тип кожи, стиль и предпочтения
              
            Обычные косметические средства содержат синтетические компоненты """)
col2.markdown("""
    <div class="title">
        <span class="pink-text">целевая аудитория</span>
    </div>
""", unsafe_allow_html=True)
col2.markdown("Люди, которым важен правильный выбор косметики, будь то с точки зрения здоровья, ухода за кожей или предпочтений в отношении ингредиентов.")
col2.markdown("""
    <div class="title">
        <span class="pink-text">технологии</span>
    </div>
""", unsafe_allow_html=True)
col2.markdown("Компьютерное зрение, генеративный ИИ, NLP & LLM, сегментация изображений")

with st.container(height=500, border=True):
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