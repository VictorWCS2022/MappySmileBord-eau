import streamlit as st
import mysql.connector
import pandas as pd 
import math
import numpy as np
import requests
import matplotlib.pyplot as plt 
import seaborn as sns 
import folium
from folium  import plugins
from folium import features
# from folium.plugins import MarkerCluster
# from folium.plugins import HeatMap

import plotly.express as px 

import pymysql
from sqlalchemy import create_engine


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * from mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")


st.title('Hello Wilders, welcome to my application!')
st.write('coucou coucou')    
    