import random

x=random.randint(1,6)
y=random.randint(1,6)
z=random.randint(1,6)

wynik = "Rzut! Wypadły {}, {} i {}.Suma rzutów to:{}"
print(wynik.format(x,y,z,(x+y+z)))