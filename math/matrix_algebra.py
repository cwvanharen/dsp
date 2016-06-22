# Matrix Algebra
import numpy as np 

A = np.matrix([[1., 2, 3], [2, 7, 4]])
B = np.matrix([[1., -1],[0, 1]])
C = np.matrix([[5., -1], [9, 1], [6, 0]])
D = np.matrix([[3., -2, -1], [1, 2, 3]])
u = np.matrix([6., 2, -3, 5])
v = np.matrix([3., 5, -1, 4])
w = np.matrix([[1.], [8], [0], [5]])

print '1.1-6'
print A.shape
# (2, 3)
print B.shape
# (2, 2)
print C.shape
# (3, 2)
print D.shape
# (2, 3)
print u.shape
# (1, 4)
print w.shape
# (4, 1)

print '2.1',
print u + v
# [[ 9.  7. -4.  9.]]

print '2.2',
print u - v
# [[ 3. -3. -2.  1.]]

print '2.3',
print 6 * u
# [[ 36.  12. -18.  30.]]

print '2.4',
print np.multiply(u, v)
# [[ 18.  10.   3.  20.]]

print '2.5',
print np.linalg.norm(u)
 # Square root of 74 ~ 8.60232526704

print '3.1'
# A + C (not defined, returns ValueError)

print '3.2'
print A - np.transpose(C)
# [[-4. -7. -3.]
# [ 3.  6.  4.]]

print '3.3'
print np.transpose(C) + (3 * D)
# [[ 14.   3.   3.]
# [  2.   7.   9.]]

print '3.4'
print np.dot(B, A)
# [[-1. -5. -1.]
# [ 2.  7.  4.]]

print '3.5' # Not defined, ValueError
# print np.dot(B, np.transpose(A))

print '3.6' # Not defined
# print np.dot(B, C)

print '3.7'
print np.dot(C, B)
# [[ 5. -6.]
# [ 9. -8.]
# [ 6. -6.]]

print '3.8'
print np.linalg.matrix_power(B, 4)
# [[ 1. -4.]
# [ 0.  1.]]

print '3.9'
print np.dot(A, np.transpose(A))
# [[ 14.  28.]
# [ 28.  69.]]

print '3.10'
print np.dot(np.transpose(D), D)
# [[ 10.  -4.   0.]
# [ -4.   8.   8.]
# [  0.   8.  10.]]