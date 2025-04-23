import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# streamlit run "/Users/zacharyfalzone/Documents/Southern CT University/Data Visualization/FinalProjectCoding/FinalProject.py"

df = pd.read_csv('https://raw.githubusercontent.com/zachjf9/finalProjectDSC205/refs/heads/main/cbb.csv')
duke_df = df[(df['TEAM'] == 'Duke') & (df['YEAR'] >= 2014)].sort_values('YEAR')
unc_df = df[(df['TEAM'] == 'North Carolina') & (df['YEAR'] >= 2014)].sort_values('YEAR')

st.title("Duke Men's Basketball Performance Over Ten Years- Zach, Trevor, Lisbel")

# 1

st.header("Overall Season Performance")
duke_df['Losses'] = duke_df['G'] - duke_df['W']
fig1, ax1 = plt.subplots()
ax1.bar(duke_df['YEAR'], duke_df['W'], label='Wins')
ax1.bar(duke_df['YEAR'], duke_df['Losses'], bottom=duke_df['W'], label='Losses', color='crimson')
ax1.set(title="Duke's Season Record Over Ten Years", xlabel="Year", ylabel="Games")
ax1.legend()
st.pyplot(fig1)

# 2 - used chatGPT here

st.header("Tournament Performance")
mapping = {
    'R68': 1, 'R64': 2, 'R32': 3, 'S16': 4,
    'E8': 5, 'F4': 6, 'Championship Game': 7, 'Champions': 8
}
tourney = duke_df[duke_df['POSTSEASON'].notna()][['YEAR', 'POSTSEASON']].copy()
tourney['Stage'] = tourney['POSTSEASON'].map(mapping)
fig2, ax2 = plt.subplots()
ax2.bar(tourney['YEAR'], tourney['Stage'], color='navy')
ax2.set(title="Tournament Progression Over Ten Years", xlabel="Year", ylabel="Round Reached")
ax2.set_yticks(list(mapping.values()))
ax2.set_yticklabels(list(mapping.keys()))
st.pyplot(fig2)

# 3

st.header("Offensive Rating")
fig3, ax3 = plt.subplots()
ax3.scatter(duke_df['YEAR'], duke_df['ADJOE'], color='navy')
ax3.set(title="Offensive Rating Over Ten Years", xlabel="Year", ylabel="ADJOE")
st.pyplot(fig3)

# 4

st.header("Defensive Rating")
fig4, ax4 = plt.subplots()
ax4.scatter(duke_df['YEAR'], duke_df['ADJDE'], color='navy')
ax4.set(title="Defensive Rating Over Ten Years", xlabel="Year", ylabel="ADJDE")
st.pyplot(fig4)

# 5

st.header("Duke vs UNC")
years = duke_df['YEAR']
bar_width = 0.3
fig5, ax5 = plt.subplots()
ax5.bar(years - bar_width / 2, duke_df['W'], width=bar_width, label='Duke', color='navy')
ax5.bar(years + bar_width / 2, unc_df['W'], width=bar_width, label='UNC', color='lightblue')
ax5.set(title="Duke vs UNC Wins Over Ten Years", xlabel="Year", ylabel="Wins")
ax5.set_xticks(years)
ax5.legend()
st.pyplot(fig5)
