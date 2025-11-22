import streamlit as st
import random
from components.common import load_cards

cards = load_cards()

st.title("API interne A2 – Simulation")

st.write(
    "Cette page simule le comportement d'une API interne, sans ouvrir de port externe. "
    "Elle montre les structures JSON que vous pourriez exposer."
)

endpoint = st.selectbox(
    "Choisir un endpoint interne",
    [
        "/internal_api/cards",
        "/internal_api/card/{id}",
        "/internal_api/tirage/simple",
        "/internal_api/tirage/3",
        "/internal_api/tirage/7",
        "/internal_api/tirage/saisons",
        "/internal_api/tirage/quotidien",
    ],
)

param_id = None
if endpoint.startswith("/internal_api/card/"):
    param_id = st.number_input("ID de carte (1–24)", min_value=1, max_value=24, value=1)

if st.button("Exécuter la simulation"):
    if endpoint == "/internal_api/cards":
        st.json(cards)

    elif endpoint.startswith("/internal_api/card/") and param_id is not None:
        st.json(cards.get(str(param_id), {}))

    elif endpoint == "/internal_api/tirage/simple":
        st.json({"type": "simple", "cartes": [random.randint(1, 24)]})

    elif endpoint == "/internal_api/tirage/3":
        st.json({"type": "3_cartes", "cartes": random.sample(range(1, 25), 3)})

    elif endpoint == "/internal_api/tirage/7":
        st.json({"type": "7_cartes", "cartes": random.sample(range(1, 25), 7)})

    elif endpoint == "/internal_api/tirage/saisons":
        st.json(
            {
                "type": "saisons",
                "saisons": ["printemps", "ete", "automne", "hiver"],
                "cartes": random.sample(range(1, 25), 4),
            }
        )

    elif endpoint == "/internal_api/tirage/quotidien":
        st.json(
            {
                "type": "quotidien",
                "cartes": [random.randint(1, 24)],
            }
        )
