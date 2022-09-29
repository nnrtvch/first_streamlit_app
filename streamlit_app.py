import streamlit as lit
import pandas as pd

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

import requests
lit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
lit.text(fruityvice_response.json())
# getting json and normilizing 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# making a table from json
lit.dataframe(fruityvice_normalized)
