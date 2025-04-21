import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

URL = 'https://raw.githubusercontent.com/zachjf9/finalProjectDSC205/refs/heads/main/cbb.csv'
df = pd.read_csv(URL)

duke_df = df[(df['TEAM'] == 'Duke') & (df['YEAR'] >= 2014)]

st.title("Duke's Performance Over the Last Decade - Zach, Trevor, Lisbel")

selectAViz = st.selectbox("Choose a plot:", [
    "Overall Season Performance",
    "Tournament Performance",
    "Offensive Rating",
    "Defensive Rating",
    "Duke vs UNC",
])

# 1 overall season performance

if selectAViz == "Overall Season Performance":
    st.subheader("Duke's Overall Season Record (Wins vs Losses)")
    duke_df['Losses'] = duke_df['G'] - duke_df['W']
    fig, ax = plt.subplots()
    ax.bar(duke_df['YEAR'], duke_df['W'], label='Wins')
    ax.bar(duke_df['YEAR'], duke_df['Losses'], bottom=duke_df['W'], label='Losses', color='crimson')
    ax.set_ylabel("Games")
    ax.set_xlabel("Year")
    ax.set_title("Dukes Season Wins and Losses")
    ax.legend()
    st.pyplot(fig)

# 2 tournament performance

elif selectAViz == "Tournament Performance":
    st.subheader("Duke's NCAA Tournament Results")

# 3 offensive rating

elif selectAViz == "Offensive Rating":
    st.subheader("Duke's Offensive Efficiency Over Ten Years")
    fig, ax = plt.subplots()
    ax.scatter(duke_df['YEAR'], duke_df['ADJOE'], color='blue', label='ADJOE')
    ax.set_ylabel("Offensive Efficiency")
    ax.set_xlabel("Year")
    ax.set_title("Duke's Offensive Rating Over Ten Years")
    st.pyplot(fig)

# 4 defensive rating

elif selectAViz == "Defensive Rating":
    st.subheader("Duke's Defensive Efficiency Over Ten Years")
    fig, ax = plt.subplots()
    ax.scatter(duke_df['YEAR'], duke_df['ADJDE'], color='red', label='ADJDE')
    ax.set_ylabel("Defensive Efficiency")
    ax.set_xlabel("Year")
    ax.set_title("Duke's Defensive Rating Over Ten Years")
    st.pyplot(fig)

# 5 duke vs unc

elif selectAViz == "Duke vs UNC":
    st.subheader("Duke vs UNC: Regular Season Wins")
    unc_df = df[(df['TEAM'] == 'North Carolina') & (df['YEAR'] >= 2014)]

    bar_width = 0.2
    years = duke_df['YEAR']
    x_duke = years - bar_width / 2
    x_unc = years + bar_width / 2
    fig, ax = plt.subplots()
    ax.bar(x_duke, duke_df['W'], width=bar_width, label='Duke', color='navy')
    ax.bar(x_unc, unc_df['W'], width=bar_width, label='UNC', color='lightblue')
    ax.set_xlabel("Year")
    ax.set_ylabel("Wins")
    ax.set_title("Duke vs UNC Over The Last 10 Years")
    ax.set_xticks(years)
    ax.set_xticklabels(years)
    ax.legend()
    st.pyplot(fig)
