# import matplotlib.pyplot as plt
# import pandas as pd
# import csv 
# df = pd.read_csv("D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\crime_data.csv")
# Country = df["Country"]
# Murder = df["Murder"]
# # Assault= df["Assault"]
# # UrbanPop= df["UrbanPop"]
# # Rape= df["Rape"]

# # colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# plt.bar(Country,Murder)

# plt.show



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
file_path = "D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\crime_data.csv"
df = pd.read_csv(file_path)

# Set the figure size
plt.figure(figsize=(15, 6))

# Define the width of the bars
bar_width = 0.2

# Define the x-axis positions
x = np.arange(len(df["Country"]))

# Plot bars for each crime type
plt.bar(x, df["Murder"], width=bar_width, label="Murder")
plt.bar(x + bar_width, df["Assault"], width=bar_width, label="Assault")
plt.bar(x + 2 * bar_width, df["UrbanPop"], width=bar_width, label="UrbanPop")
plt.bar(x + 3 * bar_width, df["Rape"], width=bar_width, label="Rape")

# Set x-axis labels
plt.xticks(x + 1.5 * bar_width, df["Country"], rotation=90)

# Set labels and title
plt.xlabel("Country")
plt.ylabel("Crime Rate")
plt.title("Crime Rates by Country")

# Add legend
plt.legend()

# Show the plot
plt.show()
