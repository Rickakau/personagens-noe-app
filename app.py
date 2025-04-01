import streamlit as st

def gerar_personagens_noe():
    return [
        {"nome": "Noé", "papel": "Protagonista", "descrição": "Homem justo e obediente, escolhido por Deus para construir a arca e sobreviver ao dilúvio."},
        {"nome": "Esposa de Noé", "papel": "Apoio", "descrição": "Parceira silenciosa de Noé, esteve ao seu lado durante toda a construção e o dilúvio."},
        {"nome": "Sem", "papel": "Filho de Noé", "descrição": "Um dos três filhos de Noé. Ajudou na construção da arca e repovoou a Terra após o dilúvio."},
        {"nome": "Cam", "papel": "Filho de Noé", "descrição": "Filho de Noé. Participou da construção da arca e da sobrevivência à grande catástrofe."},
        {"nome": "Jafé", "papel": "Filho de Noé", "descrição": "Também ajudou na construção da arca e sobreviveu ao dilúvio com sua família."},
        {"nome": "Povos da época", "papel": "Antagonistas", "descrição": "Zombavam de Noé e rejeitaram o aviso de Deus. Foram destruídos pelo dilúvio."},
        {"nome": "Deus", "papel": "Narrador invisível", "descrição": "Comunicou-se com Noé, trouxe o juízo sobre a humanidade e prometeu nunca mais destruir a Terra daquela forma."},
        {"nome": "Animais da Arca", "papel": "Simbolismo", "descrição": "Representam a preservação da criação e a obediência ao comando divino."}
    ]

st.set_page_config(page_title="Personagens da Arca de Noé", layout="centered")
st.title("🕊️ Personagens da História de Noé")
st.markdown("Conheça os personagens que viveram o maior recomeço da história.")

personagens = gerar_personagens_noe()
for p in personagens:
    with st.expander(f"🔹 {p['nome']} ({p['papel']})"):
        st.write(p["descrição"])
