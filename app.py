# Import de la bibliothèque streamlit
import streamlit as st


st.set_page_config(
    page_title="Mon premier streamlit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Titre de la page
st.title("Mon premier titre")

st.subheader("Mon premier sous-titre")

# Input de texte
user_input = st.text_input("Entrez votre texte")

# Affichage du texte
st.write("Vous avez entré : ", user_input)

# Bouton
bouton = st.button("Cliquez ici")

if bouton:
    st.write("Vous avez cliqué sur le bouton")
    # Affichage d'une image
    st.image('img.jpg')

# Formulaire streamlit avec champs Nom, prénom age et bouton

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)
       st.write("Outside the form")