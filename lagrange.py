from sympy import *
from tabulate import tabulate

x, y = symbols('x y')
f = 81*x**2 + y**2
g = 4*x**2 + y**2 - 9

fx = diff(f, x)
fy = diff(f, y)
gx = diff(g, x)
gy = diff(g, y)

l = symbols('l')
eqn1 = fx + l*gx
eqn2 = fy + l*gy
points = solve_poly_system([eqn1, eqn2, g], x, y, l)

data = []
for point in points:
    l = point[2]
    point = {x: point[0], y: point[1]}
    value = f.subs(point)
    data.append([tuple(point.values()), l, value])

headers = ['Point', 'Lambda', 'Value']
print(tabulate(data, headers=headers, tablefmt='github'))
