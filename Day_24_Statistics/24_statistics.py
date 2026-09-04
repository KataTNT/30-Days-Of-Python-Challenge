'''
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 24 - Statistics (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/24_Day_Statistics/24_statistics.md)
Challenger: KataTNT
'''

## Importing NumPy
# How to import numpy
import numpy as np
# How to check the version of the numpy package
print('numpy:', np.__version__)
# Checking the available methods
print(dir(np))

## Creating int numpy arrays
print('## Creating int numpy arrays')
# Creating python List
python_list = [1,2,3,4,5]

# Checking data types
print('Type:', type(python_list)) # <class 'list'>

print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

## Creating float numpy arrays
print('## Creating float numpy arrays')
python_list = [1,2,3,4,5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])

## Creating boolean numpy arrays
print('## Creating boolean numpy arrays')
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

## Creating multidimensional array using numpy
print('## Creating multidimensional array using numpy')
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

## Converting numpy array to list
print('## Converting numpy array to list')
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())

## Creating numpy array from tuple
print('## Creating numpy array from tuple')
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type(python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

## Shape of numpy array
print('## Shape of numpy array')
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10,11]])
print(three_by_four_array)
print('shape of three_by_four_array: ', three_by_four_array.shape)

## Data type of numpy array
print('## Data type of numpy array')
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)

## Size of a numpy array
print('## Size of a numpy array')
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])
print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 9


