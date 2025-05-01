import streamlit as st

st.set_page_config(page_title="IELTS Writing Assistant", layout="centered")

st.markdown("<h1 style='text-align: center; color: white; background-color: #00264d; padding: 1rem;'>IELTS Writing Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #666;'>Guided Paragraph Builder</h3>", unsafe_allow_html=True)
st.write("")

tema = st.text_input("Enter your topic:")
nivel = st.slider("Select difficulty level (1 = easy, 5 = expert)", 1, 5)

bloques = {
    "Intro": {
        1: "It is becoming increasingly clear that...",
        2: "There is growing concern about...",
        3: "Experts argue that...",
        4: "It appears...",
        5: "Growing concern..."
    },
    "Exposición": {
        1: "At its core, the issue revolves around...",
        2: "This debate focuses on...",
        3: "The key issue is...",
        4: "This relates to...",
        5: "The topic..."
    },
    "Causalidad": {
        1: "As a result, many problems have emerged.",
        2: "This has led to...",
        3: "One reason is...",
        4: "It results in...",
        5: "This caused..."
    },
    "Ejemplo": {
        1: "A clear example of this can be observed in...",
        2: "A good example is...",
        3: "For instance...",
        4: "Consider...",
        5: "For example..."
    },
    "Reflexión": {
        1: "Ultimately, this highlights the need for change.",
        2: "This suggests that...",
        3: "In the end, we must consider...",
        4: "This means...",
        5: "We conclude..."
    }
}

respuestas = {}

if tema:
    st.subheader("Complete your paragraph:")
    for nombre_bloque, niveles in bloques.items():
        prompt = niveles[nivel]
        st.markdown(f"**{nombre_bloque}**")
        st.markdown(f"*Prompt:* `{prompt}`")
        respuesta = st.text_area("Continue this part:", key=nombre_bloque)
        respuestas[nombre_bloque] = f"{prompt} {respuesta.strip()}"

    if st.button("Generate full paragraph"):
        st.subheader("Your Paragraph")
        texto_final = "\n\n".join(respuestas.values())
        st.write(texto_final)
        st.download_button("Download as .txt", data=texto_final, file_name="IELTS_paragraph.txt")
