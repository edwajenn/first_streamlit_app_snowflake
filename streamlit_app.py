import streamlit

streamlit.title('My Parents\' New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣Porridge with Pink Lady Apple')
streamlit.text('🍞Beans on Toast with Extra Anchovy')
streamlit.text('🐔Soft-Boiled Ostrich Egg')
streamlit.text("""🍌Banana with Extra Sausages""")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
