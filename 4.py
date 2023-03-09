from sympy import *

m = Matrix([[1, 0, 1], [2, 3, 4], [-1, -3, -3]])

# Find rank of given matrix
print(m.rank())

# Show resulting matrix with zero rows (if any)
print(m.rref()[0])
