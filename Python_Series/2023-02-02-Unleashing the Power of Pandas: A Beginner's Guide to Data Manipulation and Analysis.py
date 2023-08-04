# Pandas is a powerful, open-source Python library for data manipulation and analysis.
# Here are some of the most commonly used methods in the pandas library:

'''pd.read_csv(filepath): This method reads a CSV file and converts it into a DataFrame, which is the primary data structure used in Pandas.'''
import pandas as pd

data = pd.read_csv('data.csv')

'''DataFrame.head(): This method returns the first n rows of a DataFrame, where n is 5 by default. It's a useful method for quickly previewing the data.'''
data.head()

'''DataFrame.info(): This method provides a concise summary of a DataFrame, including the number of rows, number of columns, column data types, and memory usage.'''
data.info()

'''DataFrame.describe(): This method provides summary statistics of the numerical columns in a DataFrame, including the count, mean, standard deviation, minimum, and maximum.'''
data.describe()

'''DataFrame.columns: This attribute returns the column labels of a DataFrame.'''
data.columns

'''DataFrame.groupby(by): This method groups the rows of a DataFrame by the values in one or more columns, and applies a function to the grouped data.'''
data.groupby('column_name').mean()

'''DataFrame.sort_values(by, axis, ascending, inplace): This method sorts the rows of a DataFrame by the values in one or more columns. The by parameter specifies the column(s) to sort by, the axis parameter specifies 0 or 'index' for sorting rows and 1 or 'columns' for sorting columns, and the ascending parameter specifies whether to sort in ascending or descending order.'''
data.sort_values(by='column_name', ascending=False)

'''DataFrame.to_csv(filepath): This method writes a DataFrame to a CSV file.'''
data.to_csv('data_new.csv')
