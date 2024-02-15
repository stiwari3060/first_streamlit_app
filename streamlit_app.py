import streamlit
streamlit.title('My son New Healthy Diner')
streamlit.header('Breakfast Favourite Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Changes are appearing')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

