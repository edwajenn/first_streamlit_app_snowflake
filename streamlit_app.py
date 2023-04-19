import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

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

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
st.header('Fruityvice Fruit Advice!')
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please choose a pre-existing fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
    
   
except URLError as e:
  st.error()

# Start of Snowflake

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("SELECT * from fruit_load_list")
        return my_cur.fetchall()
if st.button('Get fruit load list!'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    st.dataframe(my_data_rows)

    
    
add_my_fruit = st.text_input('What fruit would you like to add?')

def insert_row_snowflake(add_my_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("Insert into fruit_load_list values:" + add_my_fruit)
        return "Thanks for adding " + add_my_fruit +"!"

if st.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
    back_from_function3 = insert_row_snowflake(add_my_fruit)
    st.text(back_from_function)
    

