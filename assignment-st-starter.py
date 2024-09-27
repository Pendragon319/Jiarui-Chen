import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Titan App by Mingzhe Liu')

df = pd.read_csv('train.csv')

fig, ax = plt.subplots(1, 3, figsize=(15, 5))

Pclass1 = df[df['Pclass'] == 1]['Fare']
Pclass2 = df[df['Pclass'] == 2]['Fare']
Pclass3 = df[df['Pclass'] == 3]['Fare']
ax[0].boxplot(Pclass1)
ax[1].boxplot(Pclass2)
ax[2].boxplot(Pclass3)

for i in range(3):
    ax[i].set_ylabel('Fare')
    ax[i].set_xticks([])
ax[0].set_xlabel('Pclass 1')
ax[1].set_xlabel('Pclass 2')
ax[2].set_xlabel('Pclass 3')

st.pyplot(fig)
