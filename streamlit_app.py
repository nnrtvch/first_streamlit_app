import streamlit as lit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

lit.title('My parents new Healthy Menu')
lit.header('Breakfast Favorites')
lit.text('🥣 Omega 3 & Blueberry Oatmeal')
lit.text('🥗 Kale, Spinach & Rocket Smoothie')
lit.text('🐔 Hard-Boiled Free-Range Egg') 
lit.text('🥑🍞 Avocado Toast')   
lit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected  = lit.multiselect('Pick some fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
lit.dataframe(fruits_to_show)

lit.header("Fruityvice Fruit Advice!")

fruit_choice = lit.text_input('What fruit would you like information about?','Kiwi')
lit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# getting json and normilizing 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# making a table from json
lit.dataframe(fruityvice_normalized)
lit.stop()

my_cnx = snowflake.connector.connect(**lit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
lit.header("Fruit load list contains:")
lit.dataframe(my_data_row)


add_my_fruit = lit.text_input('What fruit would you like to add?','Kiwi')
lit.write('The user entered ', fruit_choice)
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
