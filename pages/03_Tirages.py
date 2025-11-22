import streamlit as st
import random
from components.common import (
    load_cards,
    afficher_carte,
    interpretation_generale,
    interpretation_generative_poetique,
    export_pdf_single_page
)

cards = load_cards()

st.title("Tirages Divinatoires – Version Complète")


# -------------------------
# UTILITAIRE : AFFICHAGE COMPLET D'UNE CARTE
# -------------------------
def afficher_carte_complete(num, container):
    c = cards[str(num)]
    afficher_carte(num, cards, container=container)

    if c.get("ombre"):
        container.markdown(f"**Ombre :** {c['ombre']}")
    if c.get("lumiere"):
        container.markdown(f"**Lumière :** {c['lumiere']}")
    if c.get("archetype"):
        container.markdown(f"**Archétype :** {c['archetype']}")


# -------------------------
# TIRAGE SIMPLE
# -------------------------
st.subheader("Tirage simple – 1 carte")
if st.button("Tirer 1 carte"):
    tirage = [random.randint(1, 24)]
    c = tirage[0]

    col = st.container()
    afficher_carte_complete(c, col)

    st.markdown(interpretation_generale(tirage, cards))
    st.markdown(interpretation_generative_poetique(tirage, cards))


# -------------------------
# TIRAGE 3 CARTES
# -------------------------
st.subheader("Tirage en 3 cartes")
if st.button("Tirer 3 cartes"):
    tirage = random.sample(range(1, 25), 3)
    roles = ["Situation", "Obstacle", "Résolution"]

    cols = st.columns(3)
    for role, num, col in zip(roles, tirage, cols):
        col.markdown(f"### {role}")
        afficher_carte_complete(num, col)

    st.markdown(interpretation_generale(tirage, cards))
    st.markdown(interpretation_generative_poetique(tirage, cards))


# -------------------------
# TIRAGE DES 4 SAISONS
# -------------------------
st.subheader("Tirage des saisons – 4 cartes")
if st.button("Tirer les saisons"):
    tirage = random.sample(range(1, 25), 4)
    saisons = ["Printemps", "Été", "Automne", "Hiver"]

    cols = st.columns(4)
    for saison, num, col in zip(saisons, tirage, cols):
        col.markdown(f"### {saison}")
        afficher_carte_complete(num, col)

    st.markdown(interpretation_generale(tirage, cards))
    st.markdown(interpretation_generative_poetique(tirage, cards))


# -------------------------
# GRAND TIRAGE 7 CARTES
# -------------------------
st.subheader("Grand tirage – 7 cartes")
if st.button("Tirer 7 cartes"):
    tirage = random.sample(range(1, 25), 7)

    cols = st.columns(3)
    for i, num in enumerate(tirage):
        afficher_carte_complete(num, cols[i % 3])

    st.markdown(interpretation_generale(tirage, cards))
    st.markdown(interpretation_generative_poetique(tirage, cards))

    pdf = export_pdf_single_page(tirage, cards)
    st.download_button(
        "Télécharger en PDF Gold Deluxe",
        data=pdf,
        file_name="tirage_7_cartes.pdf",
        mime="application/pdf",
    )


# -------------------------------------------------
# TIRAGES SPIRITUELS SPÉCIAUX – MISSION D’ÂME, ÂME-SOEUR, CHEMIN DE VIE
# -------------------------------------------------

# Mission d'âme
st.subheader("Mission d’Âme – 3 cartes")
if st.button("Tirage Mission d’Âme"):
    roles = ["Dons innés", "Défi d’incarnation", "Direction de l’âme"]
    tirage = random.sample(range(1, 25), 3)

    cols = st.columns(3)
    for role, num, col in zip(roles, tirage, cols):
        col.markdown(f"### {role}")
        afficher_carte_complete(num, col)

    st.markdown(interpretation_generative_poetique(tirage, cards))


# Âme-Sœur
st.subheader("Âme-Sœur – 2 cartes")
if st.button("Tirage Âme-Sœur"):
    roles = ["Énergie personnelle", "Énergie de l'autre"]
    tirage = random.sample(range(1, 25), 2)

    cols = st.columns(2)
    for role, num, col in zip(roles, tirage, cols):
        col.markdown(f"### {role}")
        afficher_carte_complete(num, col)

    st.markdown(interpretation_generative_poetique(tirage, cards))


# Chemin de vie (7 cartes)
st.subheader("Chemin de Vie – 7 cartes")
if st.button("Tirage Chemin de Vie"):
    roles = [
        "Racine", "Défi majeur", "Ressource",
        "Leçon karmique", "Direction intérieure",
        "Allié", "Accomplissement"
    ]
    tirage = random.sample(range(1, 25), 7)

    cols = st.columns(3)
    for role, num, col in zip(roles, tirage, cols):
        col.markdown(f"### {role}")
        afficher_carte_complete(num, col)

    st.markdown(interpretation_generative_poetique(tirage, cards))
