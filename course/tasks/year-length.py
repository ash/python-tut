import math

r = int(input('Distance from Sun, km: '))
v = int(input('Planet\'s speed, km/h: '))

orbit_length = 2 * math.pi * r
days = orbit_length / v / 24

print('One year lasts ' + str(int(days + 0.5)) + ' days')

# Earth
# 149.600.000
# 108.000
