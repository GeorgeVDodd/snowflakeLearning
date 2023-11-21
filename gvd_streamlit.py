import streamlit
import pandas 
import snowflake.connector 
import requests
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Blueberry Oatmeal')
streamlit.text('Kale, Spinach and Rocket Smoothie') 
streamlit.text('Hard Boiled Free-Range Egg') 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruitvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?')
# removedstreamlit.write('The user entered ', fruit_choice)
if not fruit_choice: 
  streamlit.error("please select a fruit to get more information.") 
else: 
  back_from_function = get_fruityvice_data(fruit_choice)
  streamlit.dataframe(fruityvice_normalized)
streamlit.error()

# allow the user to add a fruit to the list 
def insert_row_snowflake(new_fruit)
  with my_cur = my_cnx.cursor() as my_cur 
  my_cur.execute("Insert into the fruit_load_list value ('" + ???? + "')")
  return "Thanks for adding" + new_fruit 

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a Fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)

streamlit.stop()

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list:")
streamlit.dataframe(my_data_rows)

add_my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
add_my_fruit_list = add_my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
add_my_fruit = streamlit.multiselect("Add some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
add_my_fruits_to_show = add_my_fruit_list.loc[fruits_selected]

streamlit.write('Thanks for adding ', add_my_fruit)
my_cur.execute("insert into fruit_load_list ('from streamlit')")
