import streamlit as st
import pandas as pd
import requests

st.title('My Parents\' New Healthy Dinner')
st.header('Breakfast Menu')
st.text('🥣Porridge with Pink Lady Apple')
st.text('🍞Beans on Toast with Extra Anchovy')
st.text('🐔Soft-Boiled Ostrich Egg')
st.text("""🍌Banana with Extra Sausages""")
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# inserting multi-select option
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)

st.header('Fruity Vice Fruity Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/{fruits_selected}")
st.text(fruityvice_response.json())
