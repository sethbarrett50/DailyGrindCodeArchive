# Matplotlib is a powerful data visualization library in Python that allows you to create a wide variety of plots and charts. 
# One of the most basic and widely used plots in Matplotlib is the line plot. Line plots are used to display the relationship between two numerical variables, such as time and temperature. 
# To create a line plot in Matplotlib, you will first need to import the pyplot module from the matplotlib library. 
# Then, you can use the plot() function to create a line plot of your data.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 2, 8, 4]

plt.plot(x, y)
plt.show()

# Another popular plot in Matplotlib is the scatter plot, which is used to display the relationship between two numerical variables. 
# Scatter plots are useful for visualizing the distribution of data and identifying patterns and outliers. 
# To create a scatter plot in Matplotlib, you can use the scatter() function.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 2, 8, 4]

plt.scatter(x, y)
plt.show()

# Another important aspect of Matplotlib is the ability to customize plots with different styles and options. 
# For example, you can change the color, line style, and marker style of your plot using the color, linestyle, and marker parameters.
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [5, 7, 2, 8, 4]

plt.plot(x, y, color='green', linestyle='dashed', marker='o')
plt.show()