import streamlit as st
import random
from components.common import load_cards, export_pdf_single_page, afficher_carte

cards = load_cards()

st.title("Export PDF Gold Deluxe")

st.write(
    "Vous pouvez générer un PDF clair-or illustré d’un tirage aléatoire de 3 ou 7 cartes."
)

mode = st.selectbox(
    "Type de tirage pour le PDF",
    ["3 cartes", "7 cartes"],
)

if st.button("Générer le tirage + PDF"):
    if mode == "3 cartes":
        tirage = random.sample(range(1, 25), 3)
    else:
        tirage = random.sample(range(1, 25), 7)

    st.subheader("Aperçu du tirage")
    cols = st.columns(3)
    for idx, num in enumerate(tirage):
        afficher_carte(num, cards, container=cols[idx % 3])

    pdf_buffer = export_pdf_single_page(tirage, cards)
    st.download_button(
        "Télécharger le PDF Gold Deluxe",
        data=pdf_buffer,
        file_name="tirage_gold_deluxe.pdf",
        mime="application/pdf",
    )
