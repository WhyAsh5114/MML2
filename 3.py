from sympy import *

matrix = Matrix([[1, 0, 1], [2, 3, 4], [-1, -3, -3]])
print(matrix)

echelon_form = matrix.rref()
print(echelon_form)
