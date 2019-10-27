import math

a = 3
b = 4
c = 5
x = (a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c)
pole = math.sqrt(x) / 4

txt = 'Pole wynosi {}'

print(txt.format(pole))
