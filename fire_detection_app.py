import streamlit as st
import requests
import time

url = 'http://localhost:5000/get_data' 


placeholder = st.empty()

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        placeholder.write(f"Received data: {data['data']}")
    else:
        placeholder.write("Error fetching data.")
    
    time.sleep(2)  
