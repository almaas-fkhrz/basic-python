import math
print("persamaan kuadrat")

a = int(input('masukkan nilai a : '))
b = int(input('masukkan nilai b : '))
c = int(input('masukkan nilai c : '))

d = (b**2) - (4*a*c)

x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)

print('x1 = {0} , x2 = {1}'.format(x1, x2))