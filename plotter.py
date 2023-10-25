import csv
import numpy as np
import matplotlib.pyplot as plt

#x = list()
y = list()
with open ('Exchange_r.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        #x.append(int(row[1]))
        for month in range(2,14):
            y.append(row[month])
x = np.arange(0, 48, 1)
plt.plot(x, y)

