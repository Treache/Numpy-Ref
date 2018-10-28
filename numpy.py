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

# Generating Matrices to work with

Z = np.zeros(10) => # [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.] => An array of zeros
Z = np.zeros((10, 10)) # [[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.], => A 10 by 10 Matrix with elements of 0
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       #  [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]

O = np.ones((10, 10))  # [[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.], => A 10 by 10 Matrix with elements of 1
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       #  [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]]

R = np.random.random((10, 10))  # => A 10 by 10 Matrix of random numbers (Uniformly distributed numbers between 0 and 1)
# [[0.43680105, 0.67054813, 0.46066354, 0.44664021, 0.26678115, 0.11314286, 0.10844055, 0.63050885, 0.27239895, 0.514362  ],
#  [0.81994431, 0.27528879, 0.31450672, 0.2402645 , 0.29726854, 0.62592427, 0.590267  , 0.37661295, 0.36349886, 0.05648491],
#  [0.01139133, 0.80641269, 0.5597074 , 0.98998415, 0.02811984, 0.9687394 , 0.26349025, 0.08540379, 0.58433174, 0.30629279],
#  [0.33278772, 0.54914931, 0.68346328, 0.00902739, 0.15435736, 0.25330718, 0.97060717, 0.76966729, 0.28054412, 0.41110606],
#  [0.13690156, 0.49863663, 0.8610158 , 0.72749458, 0.60764712, 0.20835044, 0.44493877, 0.54864977, 0.9387541 , 0.90185649],
#  [0.68810127, 0.10051352, 0.73984721, 0.48543647, 0.83603894, 0.02080714, 0.96721844, 0.42252876, 0.05578865, 0.8422334 ],
#  [0.02523607, 0.18456941, 0.69164703, 0.46079763, 0.22778861, 0.6886072 , 0.33680807, 0.36131755, 0.68102108, 0.67914145],
#  [0.45201343, 0.71800092, 0.60188429, 0.49032571, 0.87164761, 0.66210172, 0.54071404, 0.58282653, 0.59032766, 0.96814042],
#  [0.04412025, 0.80905661, 0.3843903 , 0.82879237, 0.33723974, 0.35911627, 0.05608102, 0.44377264, 0.28303822, 0.41713616],
#  [0.83283184, 0.86393008, 0.36504784, 0.10729737, 0.65958276, 0.45627155, 0.76704645, 0.62258565, 0.29417281, 0.87406447]]


G = np.random.randn((10, 10)) # X => This fails and returns an error
# Except other functions, randn function takes each dimention as seperate arguments not a tuple
G = np.random.randn(10, 10) # A Gaussian distributed random numbers ( Wikth means 0 and variance 1)
# [[-1.21185862,  0.33368727, -1.35279919, -0.7925704 , -1.45802625, 0.82801379,  0.19982844, -0.60748023, -1.0128342 ,  0.07325186],
#  [-0.3534653 ,  1.9345627 , -0.31164283,  1.36453597, -0.15166242, 1.21483021,  0.7815945 ,  0.25348261, -0.04826325,  0.36112567],
#  [ 0.21178518,  1.5864453 ,  0.61207435,  0.23552358, -0.77218069, 1.51420447, -0.34238478, -0.42877609,  3.06563661, -0.65123177],
#  [-0.36938199,  1.5729564 ,  1.46767292,  1.39539058, -2.58403079, 0.33184808, -0.84891263, -0.47371598,  0.41805182, -0.28020697],
#  [-0.5610131 , -0.85351789,  0.37956409,  1.44173012, -0.09393412, -0.43176507, -0.54393644,  0.24342441,  0.73448318,  1.18119496],
#  [ 0.02974791, -0.3726981 , -0.78765649,  0.07488601, -2.71829108, -2.16756416, -0.17923638, -1.55378493, -1.76074072,  1.1686108 ],
#  [ 1.76129999,  0.94494401, -0.52423802, -0.14647746, -1.06343193, -0.20799751,  0.13566515,  0.27051795, -1.14668706,  0.31858815],
#  [ 0.19952021,  0.28579737, -0.36997821, -0.99755813,  0.38551013, 0.90185384,  0.57298659, -0.23496927,  0.66122995,  1.07208792],
#  [-0.01564732,  0.13427468,  1.19242995, -1.31134885, -0.10895393, 1.57587278, -0.49842436, -0.09538358,  0.44466065,  0.07849065],
#  [-0.53921666,  0.46420597,  0.34608465, -0.925634  ,  0.75039127, -0.02418689,  0.87278479, -0.80832377,  0.7035707 ,  0.44478424]]

# Calculate statistics
G.mean() # 0.04433675513444488 => Gives us the mean
G.var()  # 0.9387452750726986  => Gives us the variance

# Matrix Products

# O     Matrix multiplication
# O     Requirement: inner dimentions must match
# O     If we have A of size (2,3) and B of size (3,3)
# O     We can multiply AB (Inner dimention is 3)
# O     We cannot multiply BA (Inner dimenstion is 3 / 2)

# A * B is the element-wise multiplication so A and B both has to be of the same size
# A.dot(B) however, is the matrix multiplication

# MORE MATRIX OPERATIONS
A = np.array([ [1, 2], [3, 4] ]) #  [1 | 2]
                                 #  [3 | 4]
Ainv = np.linalg.inc(A) # => Invert of A 
# [[-2. ,  1. ],
#  [ 1.5, -0.5]]

np.linalg.det(A) # -2.0000000000000004 => Matrix Determinant 


##################################################################################################
np.diag(A)       # [1, 4]              => Diagonal Elements

np.diag([1, 2])  # [[1, 0],
                 #  [0, 2]]
 #### **** If you pass a 2D array to the diag function, it will return a 1D array of the diagonal 
 ####      elements of that array. If you pass a vector to the diag function, it wil return
 ####      a 2D array where all the non diagonal elements are zero

##################################################################################################

