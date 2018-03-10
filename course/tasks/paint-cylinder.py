import math

d = float(input('Diameter: '))
h = float(input('Height: '))
s = float(input('Area you can paint with one can: '))

top_area = math.pi * d**2 / 4 
cylinder_area = math.pi * d * h
total_area = top_area * 2 + cylinder_area

cans_n = int(total_area / s + 0.5)
print('You need ' + str(cans_n) + ' cans')
