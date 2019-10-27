'''
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
'''
import math
# ustal promień koła i PI
r = 5
x = math.pi


# oblicz pole i obwód
p = x * (r ** 2)
l = 2 * r * x

# wyświetl rezultaty
pole = "Pole koła o promieniu {} wynosi {}"
obwod = " Obwód koła o promieniu {} wynosi {} "

print(pole.format(r, p))

print(obwod.format(r, l))