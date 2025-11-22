import streamlit as st
import os

st.set_page_config(page_title="Arcana FX++ Clair-Or – V12.1", layout="wide")

css_path = os.path.join("theme", "arcana_fx.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Particules décoratives dorées
particles_html = "<div class='mystic-particles'>" + \
    "\n".join(
        f"<div class='particle' style='left:{i*4}%; animation-delay:{i*0.6}s;'></div>"
        for i in range(1, 20)
    ) + "</div>"

st.markdown(particles_html, unsafe_allow_html=True)

st.title("Arcana FX++ Clair Mystique – Version 12.1 Finale")

st.write(
    "Bienvenue dans votre système de tirage divinatoire complet. "
    "Utilisez le menu de la barre latérale pour accéder à la galerie des cartes, "
    "aux différents tirages, à l’export PDF et à l’API interne."
)
