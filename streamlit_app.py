import streamlit as st
import pandas as pd

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
st.multiselect("Pick some fruits:", list(my_fruit_list.index))
st.dataframe(my_fruit_list)
