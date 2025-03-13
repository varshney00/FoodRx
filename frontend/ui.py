import streamlit as st
import requests

st.title("FoodRx - Recipe Finder")

diet = st.text_input("Enter a dietary restriction (e.g., vegan, gluten-free):")

if st.button("Find Recipes"):
    response = requests.get("http://127.0.0.1:8000/recipes/", params={"diet": diet})
    if response.status_code == 200:
        recipes = response.json()["recipes"]
        if recipes:
            for recipe in recipes:
                st.subheader(recipe["name"])
                st.write("**Ingredients:**", ", ".join(recipe["ingredients"]))
                st.write("**Instructions:**")
                for step in recipe["instructions"]:
                    st.write(f"- {step}")
        else:
            st.write("No recipes found for this dietary restriction.")
    else:
        st.write("Error fetching recipes.")
