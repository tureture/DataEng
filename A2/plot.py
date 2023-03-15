import matplotlib.pyplot as plt
import numpy as np
import os


# Read file out.txt
with open('A2/out.txt', 'r') as f:
    data = f.readlines()

x = []
y = []
for row in data:
    print(row.split())
    x.append(row[0])
    y.append(int(row[2]))

# Plot the data
plt.bar(x,y)
plt.title("Frequency of each first letter bar graph")
plt.show()