import streamlit
streamlit.title('My son New Healthy Diner')
streamlit.header('Breakfast Favourite Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Changes are appearing')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
--streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
--streamlit.dataframe(my_fruit_list)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Lime'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
