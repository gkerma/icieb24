import streamlit as st
from components.common import load_cards, afficher_carte

cards = load_cards()

st.title("Galerie des 24 cartes")

cols = st.columns(3)

for i in range(1, 25):
    c = cards[str(i)]
    with cols[(i - 1) % 3]:
        if st.button(c["nom"], key=f"btn_{i}"):
            st.session_state.modal = i
        st.image("images/" + c["image"], width=180)

if "modal" in st.session_state:
    num = st.session_state.modal
    c = cards[str(num)]
    with st.popover(f"Détails – {c['nom']}"):
        afficher_carte(num, cards, width=260)
        if st.button("Fermer"):
            del st.session_state.modal
