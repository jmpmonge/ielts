import streamlit as st

st.set_page_config(page_title="IELTS Writing Assistant", layout="centered")

# Título principal
st.markdown("<h1 style='text-align: center;'>IELTS Writing Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>Your personal writing and vocabulary coach</h4>", unsafe_allow_html=True)
st.write("")

# Menú principal en columnas
col1, col2 = st.columns(2)

with col1:
    if st.button("✍️ Start Writing"):
        st.switch_page("components/bloque_writer.py")

    if st.button("📚 Expression Review"):
        st.switch_page("components/vocab_card.py")

with col2:
    if st.button("🧠 Practice & Recall"):
        st.switch_page("modules/evaluator.py")

    if st.button("📊 My Progress"):
        st.switch_page("modules/level_estimator.py")

st.write("---")

# Pie de página
st.markdown("<small style='color: gray;'>Developed with Streamlit – AI-powered feedback included</small>", unsafe_allow_html=True)
