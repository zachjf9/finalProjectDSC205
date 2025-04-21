import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

URL = 'https://raw.githubusercontent.com/iantonios/dsc205/refs/heads/main/bike_sharing.csv'
df = pd.read_csv(URL)