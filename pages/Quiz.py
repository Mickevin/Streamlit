# Création d'un Quiz avec streamlit
import streamlit as st

st.title("Quiz de culture générale")

# Création d'un formulaire
with st.form("my_form"):

    reponse1 = st.text_input("Quelle est la capitale de la France ?")

    bouton = st.form_submit_button("Valider")

    if bouton:
        if reponse1.lower() == "paris":
            st.write("Bonne réponse")
        else:
            st.write("Mauvaise réponse")