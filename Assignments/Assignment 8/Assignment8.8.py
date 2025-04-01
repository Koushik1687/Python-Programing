import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


file_path = "D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\crime_data.csv"
df = pd.read_csv(file_path)

plt.figure(figsize=(15, 6))

bar_width = 0.2

x = np.arange(len(df["Country"]))

plt.bar(x, df["Murder"], width=bar_width, label="Murder")
plt.bar(x + bar_width, df["Assault"], width=bar_width, label="Assault")
plt.bar(x + 2 * bar_width, df["UrbanPop"], width=bar_width, label="UrbanPop")
plt.bar(x + 3 * bar_width, df["Rape"], width=bar_width, label="Rape")

plt.xticks(x + 1.5 * bar_width, df["Country"], rotation=90)

plt.xlabel("Country")
plt.ylabel("Crime Rate")
plt.title("Crime Rates by Country")

plt.legend()

plt.show()
