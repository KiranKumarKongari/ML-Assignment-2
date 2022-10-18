# Using NumPy create random vector of size 15 having only Integers in the range 1-20.
# 1. Reshape the array to 3 by 5
# 2. Print array shape.
# 3. Replace the max in each row by 0


# Imported the numpy package
import numpy as np

# Created random vector named x of size 15 having only Integers in the range 1-20.
x = np.random.randint(1, 20, 15)
print("\nRandom vector of size 15 having integers in the range of 1-20 is : \n", x)

# Reshaped the array to 3 by 5 using reshape function.
reshapedArray = x.reshape((3, 5))
print("\nReshaped 3 by 5 array is : \n", reshapedArray)

# Finding the shape of the using the shape function and displayed the result.
shape = np.shape(reshapedArray)
print("\nShape of the array is : ", shape)

# Got the max value for each row using amax function.
maxNum = np.amax(reshapedArray, axis=1)

# Then replaced the max value of each row with 0 using where and isin function and displayed the resultant matrix
newArray = np.where(np.isin(reshapedArray, maxNum), 0, reshapedArray)
print("\nArray after replacing the max in each row by 0 is : \n", newArray)


