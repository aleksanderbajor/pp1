
wzrost = int(input("Podaj swój wzrost w cm:"))
masa = int(input("Podaj swoją masę w kg:"))



BMI = masa/(wzrost/100)**2
print(BMI)

if BMI > 24.9:
    print("nadwaga")
elif BMI < 19.5:
    print("niedowaga")
else:
    print("Waga prawidłowa")