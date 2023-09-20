valeur = 1000
for i in range(31) :
    temperature = float(input("Veuillez entrer une température "))
    if(temperature < valeur):
        valeur = temperature
print("La valeur la plus petite est " + str(valeur))