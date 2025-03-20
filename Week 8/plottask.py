'''
plottask.py

The objective of this program is to displays

    - A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    - A plot of the function  h(x)=x3 in the range 0 to 10, 

Author: Loic Bagnoud
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn

data = np.random.normal(5, 2, 1000)


plt.hist(data, bins=25, edgecolor = "black", color='b')
plt.grid(axis = 'y', color = 'darkblue', linestyle = '--', linewidth = 0.2)
plt.title("Histogram of Distributions")
plt.xlabel("Counts")
plt.ylabel("Probability")

plt.figure()
x = np.sort(np.random.randint(0, 11, 100))
y = x**3
plt.plot(x, y, color="red", label="h(x) = x^3")
plt.grid(axis = 'y', color = 'darkblue', linestyle = '--', linewidth = 0.2)
plt.title("Plot of h(x) = x^3")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.legend()
plt.show()



# ChatGPT - proposed plt.figure: Using plt.figure(): The command plt.figure() simply creates a new window (or figure) for your plot. It helps to separate different visualizations, so you could have one figure for your histogram and another for your function plot. This keeps your plots clear and uncluttered.

# https://matplotlib.org/stable/gallery/color/named_colors.html - For colours