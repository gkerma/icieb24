import streamlit as st
import random
from components.common import load_cards, afficher_carte, interpretation_generale, export_pdf_single_page

cards = load_cards()

st.title("Tirages divinatoires")

st.markdown("Choisissez un type de tirage :")

# Tirage simple
if st.button("Tirage simple (1 carte)"):
    tirage = [random.randint(1, 24)]
    st.subheader("Résultat du tirage simple")
    afficher_carte(tirage[0], cards)
    st.markdown(interpretation_generale(tirage, cards))

# Tirage 3 cartes
if st.button("Tirage en 3 cartes"):
    tirage = random.sample(range(1, 25), 3)
    st.subheader("Tirage en 3 cartes")
    positions = ["Situation", "Obstacle", "Résolution"]
    cols = st.columns(3)
    for pos, num, col in zip(positions, tirage, cols):
        col.markdown(f"### {pos}")
        afficher_carte(num, cards, container=col)
    st.markdown(interpretation_generale(tirage, cards))

# Tirage des saisons
if st.button("Tirage des 4 saisons"):
    tirage = random.sample(range(1, 25), 4)
    saisons = ["Printemps", "Été", "Automne", "Hiver"]
    st.subheader("Tirage des saisons")
    cols = st.columns(4)
    for saison, num, col in zip(saisons, tirage, cols):
        col.markdown(f"### {saison}")
        afficher_carte(num, cards, container=col)
    st.markdown(interpretation_generale(tirage, cards))

# Grand tirage 7 cartes
if st.button("Grand tirage 7 cartes"):
    tirage = random.sample(range(1, 25), 7)
    st.subheader("Grand tirage 7 cartes")
    cols = st.columns(3)
    for idx, num in enumerate(tirage):
        afficher_carte(num, cards, container=cols[idx % 3])

    st.markdown(interpretation_generale(tirage, cards))

    pdf_buffer = export_pdf_single_page(tirage, cards)
    st.download_button(
        "Télécharger le tirage en PDF Gold Deluxe",
        data=pdf_buffer,
        file_name="tirage_gold_deluxe.pdf",
        mime="application/pdf",
    )
