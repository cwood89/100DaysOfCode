import numpy as np

# numpy is a library used for scientific computing
# numpy can be faster than built in list functions.

# provides a multidimensional array object
a = np.array([(1, 2, 3), (4, 5, 6)])  # 2 columns and 3 rows
b = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])  # 2 columns 4 rows
b2 = b.reshape(4, 2)  # reshapes to 4 columns 2 rows

print(a.ndim)  # prints the dimension of array | 2
print(a.itemsize)  # prints the byte size of each element
print(a.dtype)  # prints data type of array
print(a.size)  # prints how many elements
print(a.shape)  # prints shape of array (2,3)
print(b.max())  # prints max value
print(b.min())  # prints minium value
print(b.sum())  # adds all elemts in array
print(b[0, 2])  # returns 3rd element in 1st row
print(b[0: 2])  # returns 3rd element in all rows
c = np.linspace(1, 3, 10)
print(c)  # prints 10 values between 1 and 3
