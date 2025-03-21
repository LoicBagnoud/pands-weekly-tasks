'''
plottask.py

The objective of this program is to displays

    - A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
    - A plot of the function  h(x)=x3 in the range 0 to 10, 

Author: Loic Bagnoud
'''

# The first thing that I needed to do, was import the packages I needed, in this case, numpy and pyplot
import numpy as np
import matplotlib.pyplot as plt

# This numpy function is to get a normal distribution and assign it to a variable called data
data = np.random.normal(5, 2, 1000)

# Then, I went ahead with the creation of the actual plots. First the histogram.
# For these two, I have the number of bins, the edge color as well as the bars themselves. I went and searched for the actual codes for the colours.
plt.hist(data, bins=25, edgecolor = "black", color='cornflowerblue')
plt.grid(axis = 'y', color = 'darkblue', linestyle = '--', linewidth = 0.2)

# I wasn't sure what titles to give honestly. I went with generic things such as Histogram of Distributions. 
# For the x and y label I just went with the basic descriptions. 
plt.title("Histogram of Distributions")
plt.xlabel("Counts")
plt.ylabel("Probability")

# This was to save it as a png file
plt.savefig('Histogram of Distributions.png')

# This one was more difficult. First of all, I wasn't sure what plot to go for. Had to consult chatgpt for this
# and he suggested the function plt.figure(), since it allows me to create any sort of plot I need. 
plt.figure()

# Next, assigning the varibles. I used randint to once again get a range of 0 to 10. I went with 100 values and sorted them with .sort.
# The y variable was just x cubed.
x = np.sort(np.random.randint(0, 11, 100))
y = x**3

# Next came the plot itself. We have the x and y axis. I went with red this time and added a label.
plt.plot(x, y, color="red", label="h(x) = x^3")

# I added a grid since I think it makes reading the plot easier. 
plt.grid(axis = 'y', color = 'darkblue', linestyle = '--', linewidth = 0.2)

# And finally the title and legends with show at the end. 
plt.title("Plot of h(x) = x^3")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.legend()
plt.savefig(' h(x)=x3 function.png')
plt.show()



# References: 

# ChatGPT - Explanation on h(x)=x3 function 
''''
Prompt used: Can you explain in very simple terms what does 
and a plot of the function  h(x)=x3 in the range 0 to 10 means?'
'''
# ChatGPT - Explanation of .figure proposal for the second plot
'''
So would the best plot to show case this be a figure since you have plt.figure? Can't I do a normal histogram? Explain to'
me the use of .figure
'''

# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html - Getting Numpy normal distribution

# https://matplotlib.org/stable/gallery/color/named_colors.html - For colours

# https://medium.com/@brainhj/kde-true-c3d42a0c8ced - For the Seaborn curve code

# https://www.w3schools.com/python/matplotlib_grid.asp - For the plot grids