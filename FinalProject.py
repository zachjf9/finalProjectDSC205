import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# streamlit run "/Users/zacharyfalzone/Documents/Southern CT University/Data Visualization/FinalProjectCoding/FinalProject.py"

df = pd.read_csv('https://raw.githubusercontent.com/zachjf9/finalProjectDSC205/refs/heads/main/cbb.csv')
duke_df = df[(df['TEAM'] == 'Duke') & (df['YEAR'] >= 2014)].sort_values('YEAR')
unc_df = df[(df['TEAM'] == 'North Carolina') & (df['YEAR'] >= 2014)].sort_values('YEAR')

st.title("Why Duke Men's Basketball Has Performed Better Than UNC Over The Last Decade")

# 1 Duke vs UNC offensive effeciency

st.header("Duke vs UNC's Offensive Rating")
fig1, ax1 = plt.subplots()
ax1.scatter(duke_df['YEAR'], duke_df['ADJOE'], color='navy')
z = np.polyfit(duke_df['YEAR'], duke_df['ADJOE'], 1)
p = np.poly1d(z)
ax1.plot(duke_df['YEAR'], p(duke_df['YEAR']), color='navy', linestyle='--', label='Trendline')
ax1.scatter(unc_df['YEAR'], unc_df['ADJOE'], color='lightblue')
z = np.polyfit(unc_df['YEAR'], unc_df['ADJOE'], 1) 
p = np.poly1d(z)
ax1.plot(unc_df['YEAR'], p(unc_df['YEAR']), color='lightblue', linestyle='--', label='Trendline')
ax1.set(title="Duke vs UNC's Offensive Rating Over Ten Years", xlabel="Year", ylabel="ADJOE")
st.pyplot(fig1)
st.caption("This scatterplot compares Duke and UNC's offensive efficiency (ADJOE) over the last ten years, with trendlines indicating overall performance trends.")

# 2 Duke vs UNC defensive effeciency

st.header("Duke vs UNC's Defensive Rating")
fig2, ax2 = plt.subplots()
ax2.scatter(duke_df['YEAR'], duke_df['ADJDE'], color='navy')
z = np.polyfit(duke_df['YEAR'], duke_df['ADJDE'], 1)
p = np.poly1d(z)
ax2.plot(duke_df['YEAR'], p(duke_df['YEAR']), color='navy', linestyle='--', label='Trendline')
ax2.scatter(unc_df['YEAR'], unc_df['ADJDE'], color='lightblue')
z = np.polyfit(unc_df['YEAR'], unc_df['ADJDE'], 1)
p = np.poly1d(z)
ax2.plot(unc_df['YEAR'], p(unc_df['YEAR']), color='lightblue', linestyle='--', label='Trendline')
ax2.set(title="Duke vs UNC's Defensive Rating Over Ten Years", xlabel="Year", ylabel="ADJDE")
st.pyplot(fig2)
st.caption("This plot compares Duke and UNC's defensive efficiency (ADJDE) has changed over the past decade, with lower values indicating better defense.")

# 3 dukes vs unc overall season performance

st.header("Duke vs UNC's Overall Season Performance")
duke_df['Losses'] = duke_df['G'] - duke_df['W']
unc_df['Losses'] = unc_df['G'] - unc_df['W']
years = duke_df['YEAR']
bar_width = 0.3
fig3, ax3 = plt.subplots()
ax3.bar(years - bar_width / 2, duke_df['W'], width=bar_width, label='Duke', color='navy')
ax3.bar(years - bar_width / 2, duke_df['Losses'], bottom=duke_df['W'], width=bar_width,label='Duke Losses', color='darkred')
ax3.bar(years + bar_width / 2, unc_df['W'], width=bar_width, label='UNC', color='lightblue')
ax3.bar(years + bar_width / 2, unc_df['Losses'], bottom=unc_df['W'], width=bar_width,label='UNC Losses', color='crimson')
ax3.set(title="Duke vs UNC's Wins Season performance over Ten Years", xlabel="Year", ylabel="Wins")
ax3.set_xticks(years)
ax3.legend()
st.pyplot(fig3)
st.caption("This bar chart shows the number of wins and losses each season for Duke and UNC, highlighting each team's overall regular season success.")

# 4 dukes tournament progression - used chatGPT here

st.header("Duke's Tournament Performance")
mapping = {
    'R68': 1, 'R64': 2, 'R32': 3, 'S16': 4,
    'E8': 5, 'F4': 6, 'Championship Game': 7, 'Champions': 8
}
tourney = duke_df[duke_df['POSTSEASON'].notna()][['YEAR', 'POSTSEASON']].copy()
tourney['Stage'] = tourney['POSTSEASON'].map(mapping)
fig4, ax4 = plt.subplots()
ax4.bar(tourney['YEAR'], tourney['Stage'], color='navy')
ax4.set(title="Duke's Tournament Progression Over Ten Years", xlabel="Year", ylabel="Round Reached")
ax4.set_yticks(list(mapping.values()))
ax4.set_yticklabels(list(mapping.keys()))
st.pyplot(fig4)
st.caption("This bar chart displays how far Duke progressed in the NCAA Tournament each year, from early rounds to championship appearances.")

# 5 uncs tournament performance

st.header("UNC's Tournament Performance")
mapping = {
    'R68': 1, 'R64': 2, 'R32': 3, 'S16': 4,
    'E8': 5, 'F4': 6, 'Championship Game': 7, 'Champions': 8
}
tourney = unc_df[unc_df['POSTSEASON'].notna()][['YEAR', 'POSTSEASON']].copy()
tourney['Stage'] = tourney['POSTSEASON'].map(mapping)
fig5, ax5 = plt.subplots()
ax5.bar(tourney['YEAR'], tourney['Stage'], color='lightblue')
ax5.set(title="UNC's Tournament Progression Over Ten Years", xlabel="Year", ylabel="Round Reached")
ax5.set_yticks(list(mapping.values()))
ax5.set_yticklabels(list(mapping.keys()))
st.pyplot(fig5)
st.caption("This chart mirrors Duke's, showing UNC's progression through the NCAA Tournament over the last decade.")
