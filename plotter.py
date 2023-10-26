
import matplotlib.pyplot as plt

import csv

x = list()
y = list()
with open ('Exchange_r.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        x.append(int(row[0]))
        y.append(float(row[1]))

plt.plot(x, y, marker='o')    
