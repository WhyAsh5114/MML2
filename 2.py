from sympy import *

# Define function and symbols
x, y = symbols('x y')
f = x**3 - 12*x + y**3 + 3*y**2 - 9*y
print(f)

# Find all derivatives
fx = diff(f, x)
fxx = diff(fx, x)
fy = diff(f, y)
fyy = diff(fy, y)
fxy = diff(fx, y)

# Generate points
points = solve_poly_system([fx, fy], x, y)

# Try to find minimum and maximum point
max_point = None
min_point = None
for point in points:
    point = {x: point[0], y: point[1]}
    r = fxx.subs(point)
    t = fyy.subs(point)
    s = fxy.subs(point)
    d = r*t - s**2
    if d > 0:
        if r > 0 or t > 0:
            min_point = point
        if r < 0 or t < 0:
            max_point = point

# If minimum point found, print answer
if min_point:
    print(f"Minima at: {list(min_point.values())} =", f.subs(min_point))
else:
    print("Minima cannot be found")

# If maximum point found, print answer
if max_point:
    print(f"Maxima at: {list(max_point.values())} =", f.subs(max_point))
else:
    print("Maxima cannot be found")
