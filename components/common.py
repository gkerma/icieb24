import json
import os
import random
import io
from datetime import datetime

import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as PdfImage, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


DATA_PATH = "data/cards.json"
IMAGE_PATH = "images"


@st.cache_data
def load_cards(path: str = DATA_PATH) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def afficher_carte(num: int, cards: dict, container=None, width: int = 230):
    c = cards[str(num)]
    cont = container if container else st

    img_path = os.path.join(IMAGE_PATH, c["image"])
    if os.path.exists(img_path):
        cont.image(img_path, width=width)

    cont.markdown(f"### {c['nom']}")
    if c.get("symboles"):
        cont.markdown(f"**Symboles :** {c['symboles']}")
    if c.get("texte"):
        cont.markdown("**Texte inscrit :**")
        for t in c["texte"]:
            cont.markdown(f"- {t}")
    if c.get("interpretation"):
        cont.markdown(f"**Interprétation :** {c['interpretation']}")


def interpretation_generale(tirage: list[int], cards: dict) -> str:
    themes = []
    energies = []
    cycles = 0

    for num in tirage:
        txt = cards[str(num)]["interpretation"].lower()

        if "cycle" in txt:
            cycles += 1
        if "action" in txt:
            energies.append("action")
        if "abondance" in txt:
            energies.append("abondance")
        if "intuition" in txt:
            themes.append("intuition")
        if "racine" in txt or "origine" in txt:
            themes.append("origines")
        if "renaissance" in txt:
            themes.append("renaissance")
        if "protection" in txt:
            themes.append("protection")

    out = "### Interprétation générale\n"

    if cycles > 1:
        out += "- Une dynamique cyclique importante influence la situation.\n"
    if "action" in energies:
        out += "- Une action ou une décision claire est favorisée.\n"
    if "abondance" in energies:
        out += "- Une phase d’expansion positive et d’opportunités se dessine.\n"
    if "intuition" in themes:
        out += "- L’intuition est un guide central dans ce tirage.\n"
    if "origines" in themes:
        out += "- Un retour aux fondations ou aux racines est mis en lumière.\n"
    if "renaissance" in themes:
        out += "- Une renaissance intérieure ou un nouveau départ est en cours.\n"
    if "protection" in themes:
        out += "- Une énergie protectrice enveloppe ce tirage.\n"

    if out.strip() == "### Interprétation générale":
        out += "Le tirage semble neutre ou en phase de transition."

    return out


def export_pdf_single_page(tirage: list[int], cards: dict) -> io.BytesIO:
    buffer = io.BytesIO()
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Tirage – Tarot Clair-Or Gold Deluxe", styles["Title"]))
    story.append(Spacer(1, 0.3 * inch))

    for num in tirage:
        c = cards[str(num)]
        story.append(Paragraph(f"<b>{c['nom']}</b>", styles["Heading2"]))
        img_path = os.path.join(IMAGE_PATH, c["image"])
        if os.path.exists(img_path):
            story.append(PdfImage(img_path, width=2.3 * inch, height=3.4 * inch))
        if c.get("texte"):
            story.append(Paragraph("<br/>".join(c["texte"]), styles["BodyText"]))
        if c.get("interpretation"):
            story.append(Paragraph(f"<i>{c['interpretation']}</i>", styles["Italic"]))
        story.append(Spacer(1, 0.35 * inch))

    story.append(Paragraph(interpretation_generale(tirage, cards), styles["BodyText"]))
    story.append(Spacer(1, 0.3 * inch))
    story.append(Paragraph(f"Tirage généré le {datetime.now().strftime('%Y-%m-%d')}", styles["BodyText"]))

    doc = SimpleDocTemplate(buffer, pagesize=letter)
    doc.build(story)
    buffer.seek(0)
    return buffer
