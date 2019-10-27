import random

x=random.randint(1,6)

y=int(input("Podaj ile oczek wyrzucił komputer:"))

if y == x:
    print("true")
else:
    print("Komputer rzucił",int(x),"Spróbuj jeszcze raz")