import numpy as np

a = [1, 2] # A python list
b = [2, 1] # A python list

A = np.array(a) # A numpy array
B = np.array(b) # A numpy array

a + b # => [1, 2, 2, 1] | Concatinates a and b
A + B # => [3, 3] | Element wise addition as a numpy array

2 * a # => [1, 2, 1, 2] | Concatinates a with itself
2 * A # => [2, 4] | Element wise multiplication with a static number

# a ** 2 # => ERROR
A ** 2 #=> [1, 4] | Element wise power as a numpy array

np.sqrt(A) # => [1.        , 1.41421356] | Square root of every element of A as a numpy array
np.log(A)  # => [0.        , 0.69314718] | Logarithm of every element of A as a numpy array
np.exp(A)  # => [2.71828183, 7.3890561 ] | Exponential of every element of A as a numpy array

A * B      # => [2  , 2  ] | Element wise multiplication
A / B      # => [0.5, 2. ] | Element wise devision
A ** B     # => [1  , 2  ] | Element wise power
B ** A     # => [2  , 1  ] | Element wise power

np.sum(A * B) # => 4
(A * B).sum() # => 4
np.dot(A, B)  # => 4
A.dot(B)      # => 4

#   |
#   |a[1]    
#   |......O A => [1, 2]
#   |     .                         
#   |     .                                 
#   |_____._______________      
#   T    a[0]

a_magnitude = np.sqrt((A * A).sum()) # => 2.23606797749979
b_magnitude = np.linalg.norm(B)      # => 2.23606797749979

cosangle = A.dot(B) / (a_magnitude * b_magnitude) # => 0.7999999999999998
angle = np.arccos(cosangle) # => 0.6435011087932847

# A Matrix
L = [ [1, 2], [3, 4] ]

M = np.array([ [1, 2], [3, 4] ]) #  [1 | 2] 
                                 #  [3 | 4]
                                 
M.T                              #  [1 | 3]  => The transpose of the matrix (Array)
                                 #  [2 | 4]
                                 
# Accessing elements
    # List => 
L[0]    # => [1, 2]
L[0][0] # => 1
    # Matrix (Numpy 2D Array)
M[0,]   # => [1, 2]
M[0, 0] # => 1

M2 = np.matrix(L) # Numpy Matrix (depricated) => We use the numpy array instead. Even 
                  # if you see a Matrix somewhere just convert it to an array => np.array(M2)

## A Vector is just a one dimentional numpy array and
## a Matrix is really just a 2D numpy array