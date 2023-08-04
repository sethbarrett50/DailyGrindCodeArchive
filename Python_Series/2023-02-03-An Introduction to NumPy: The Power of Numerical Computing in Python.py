# NumPy is a powerful, open-source Python library for numerical computation and data manipulation.
# Here are some of the most commonly used methods in the NumPy library:

'''np.array(data, dtype=None, copy=True, order='K', subok=False, ndmin=0): This function creates an array from the given input data. The data parameter can be a list, tuple, or array-like object, and the dtype parameter specifies the data type of the resulting array. The copy parameter, if set to True, creates a copy of the input data, and the order parameter specifies the memory layout of the resulting array.'''
import numpy as np

a = np.array([1, 2, 3, 4])

'''np.zeros(shape, dtype=float, order='C'): This function returns a new array of given shape and type, filled with zeros. The shape parameter specifies the shape of the array and the dtype parameter specifies the data type of the array.'''
np.zeros((3,3))

'''np.ones(shape, dtype=None, order='C'): This function returns a new array of given shape and type, filled with ones. The shape parameter specifies the shape of the array and the dtype parameter specifies the data type of the array.'''
np.ones((2,2))

'''np.arange(start, stop, step, dtype): This function returns an array with evenly spaced values within a given range. The start parameter specifies the start of the range, the stop parameter specifies the end of the range, and the step parameter specifies the spacing between the values. The dtype parameter specifies the data type of the array.'''
np.arange(1, 10, 2)

'''np.linspace(start, stop, num, endpoint, retstep, dtype): This function returns an array with evenly spaced values within a given range. The start parameter specifies the start of the range, the stop parameter specifies the end of the range, and the num parameter specifies the number of elements in the resulting array. The endpoint parameter, if set to True, includes the end value in the range. The retstep parameter, if set to True, returns the step value used in the range. The dtype parameter specifies the data type of the array.'''
np.linspace(1, 10, 6)

'''np.random.random(size=None): This function returns random floats in the half-open interval [0.0, 1.0). The size parameter specifies the shape of the array.'''
np.random.random((3,3))

'''np.min(a, axis=None, out=None, keepdims=False): This function returns the minimum of an array or minimum along an axis. The a parameter specifies the input array, the axis parameter specifies the axis along which the minimum value is calculated and the out parameter specifies the output and the keepdims parameter, if set to True, keeps the dimensions of the input array.'''
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.min(a, axis=0)

'''np.max(a, axis=None, out=None, keepdims=False): This function returns the maximum of an array or maximum along an axis. The a parameter specifies the input array, the axis parameter specifies the axis along which the maximum value is calculated and the out parameter specifies the output and the keepdims parameter, if set to True, keeps the dimensions of the input array.'''
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.max(a, axis=0)

'''np.mean(a, axis=None, dtype=None, out=None, keepdims=False): This function returns the mean of an array or mean along an axis. The a parameter specifies the input array, the axis parameter specifies the axis along which the mean value is calculated, the dtype parameter specifies the data type of the output, the out parameter specifies the output and the keepdims parameter, if set to True, keeps the dimensions of the input array.'''
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.mean(a, axis=0)

'''np.median(a, axis=None, out=None, overwrite_input=False, keepdims=False): This function returns the median of an array or median along an axis. The a parameter specifies the input array, the axis parameter specifies the axis along which the median value is calculated, the out parameter specifies the output, the overwrite_input parameter, if set to True, allows the input array to be modified and the keepdims parameter, if set to True, keeps the dimensions of the input array.'''
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.median(a, axis=0)