import streamlit
streamlit.title("My parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 and blueberry oatmeal")
streamlit.text("Chole Chawal")
streamlit.text("🥣 🥗 🐔 🥑🍞")


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
