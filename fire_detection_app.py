import streamlit as st
import requests
import time

url = 'https://getdatafromaurdino-yiztygkiej88n2pqfcmv2y.streamlit.app/' 


placeholder = st.empty()

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        placeholder.write(f"Received data: {data['data']}")
    else:
        placeholder.write("Error fetching data.")
    
    time.sleep(2)  
