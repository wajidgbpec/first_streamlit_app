import streamlit
streamlit.title("My parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 and blueberry oatmeal")
streamlit.text("Chole Chawal")
streamlit.text("🥣 🥗 🐔 🥑🍞")


import pandas
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
