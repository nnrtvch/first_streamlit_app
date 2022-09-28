import streamlit as lit
import pandas as pd

lit.title('My parents new Healthy Menu')
lit.header('Breakfast Favorites')
lit.text('🥣 Omega 3 & Blueberry Oatmeal')
lit.text('🥗 Kale, Spinach & Rocket Smoothie')
lit.text('🐔 Hard-Boiled Free-Range Egg') 
lit.text('🥑🍞 Avocado Toast')   
lit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
lit.dataframe(my_fruit_list)
