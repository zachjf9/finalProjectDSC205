import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/zachjf9/finalProjectDSC205/refs/heads/main/cbb.csv')
duke_df = df[(df['TEAM'] == 'Duke') & (df['YEAR'] >= 2014)]

st.title("Duke Men's Basketball Performance (2014–2024) - Zach, Trevor, Lisbel")

option = st.selectbox("Choose a plot:", [
    "Overall Season Performance",
    "Tournament Performance",
    "Offensive Rating",
    "Defensive Rating",
    "Duke vs UNC"
])

# 1 season performance

if option == "Overall Season Performance":
    duke_df['Losses'] = duke_df['G'] - duke_df['W']
    fig, ax = plt.subplots()
    ax.bar(duke_df['YEAR'], duke_df['W'], label='Wins')
    ax.bar(duke_df['YEAR'], duke_df['Losses'], bottom=duke_df['W'], label='Losses', color='crimson')
    ax.set(title="Duke's Season Record Over Ten Years", xlabel="Year", ylabel="Games")
    ax.legend()
    st.pyplot(fig)

# 2 tourney performance

elif option == "Tournament Performance":
    mapping = {
        'R68': 1, 'R64': 2, 'R32': 3, 'S16': 4,
        'E8': 5, 'F4': 6, 'Championship Game': 7, 'Champions': 8
    }
    tourney = duke_df[duke_df['POSTSEASON'].notna()][['YEAR', 'POSTSEASON']].copy()
    tourney['Stage'] = tourney['POSTSEASON'].map(mapping)
    fig, ax = plt.subplots()
    ax.bar(tourney['YEAR'], tourney['Stage'], color='navy')
    ax.set(title="Tournament Progression Over Ten Years", xlabel="Year", ylabel="Round Reached")
    ax.set_yticks(list(mapping.values()))
    ax.set_yticklabels(list(mapping.keys()))
    st.pyplot(fig)

# 3 offensive rating

elif option == "Offensive Rating":
    fig, ax = plt.subplots()
    ax.scatter(duke_df['YEAR'], duke_df['ADJOE'], color='navy')
    ax.set(title="Offensive Rating Over Ten Years", xlabel="Year", ylabel="ADJOE")
    st.pyplot(fig)

# 4 defensive rating

elif option == "Defensive Rating":
    fig, ax = plt.subplots()
    ax.scatter(duke_df['YEAR'], duke_df['ADJDE'], color='navy')
    ax.set(title="Defensive Rating Over Ten Years", xlabel="Year", ylabel="ADJDE")
    st.pyplot(fig)

# 5 duke vs unc

elif option == "Duke vs UNC":
    unc_df = df[(df['TEAM'] == 'North Carolina') & (df['YEAR'] >= 2014)]
    years = duke_df['YEAR']
    bar_width = 0.3
    fig, ax = plt.subplots()
    ax.bar(years - bar_width / 2, duke_df['W'], width=bar_width, label='Duke', color='navy')
    ax.bar(years + bar_width / 2, unc_df['W'], width=bar_width, label='UNC', color='lightblue')
    ax.set(title="Duke vs UNC Wins Over Ten Years", xlabel="Year", ylabel="Wins")
    ax.set_xticks(years)
    ax.legend()
    st.pyplot(fig)
