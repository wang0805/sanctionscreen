import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

headers = {
    'X-API-Key': api_key,
    'Accept': 'application/json',
}
# address = 'LNwgtMxcKUQ51dw7bQL1yPQjBVZh6QEqsd'

# response = requests.get(
#     'https://public.chainalysis.com/api/v1/address/{}'.format(address), headers=headers)

# Input field for user to enter a value
st.title("Chainalysis Sanction API")
user_input = st.text_input("Enter a wallet address:")

# Button to trigger the API call
if st.button("Submit"):
    # Make the API call with the user input
    response = requests.get(
        'https://public.chainalysis.com/api/v1/address/{}'.format(user_input), headers=headers)

    # Display the response
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.write("Error in API call")
