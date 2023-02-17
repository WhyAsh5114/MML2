from sympy import *

# Declare x and y as special variables
x, y = symbols('x y')

# Create a function
# x^2 + 5x.sin(y) + e^(x.cos(x))
f = x**2 + 5*x*sin(y) - exp(x*cos(x))

# Print differentiation of f with respect to x
print(diff(f, x))

# Print differentiation of f with respect to y
print(diff(f, y))
