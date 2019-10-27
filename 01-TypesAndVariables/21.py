c = int(input("Podaj temperature w stopniach Celsjusza:"))

f = c*2+32

k = c+273.15

fah = 'Fahrenheita'
kal = 'Kelvina'

txt = "Temperatura w stopniach {}, dla temperatury Celsjusza równej {} stopni, wynosi około {} stopni"



print(txt.format(fah, c, f))
print(txt.format(kal, c, k))
