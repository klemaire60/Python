valeur_basse = 1000
valeur_haute = -100
for i in range(31) :
    temperature = float(input("Veuillez entrer une température "))
    if(temperature < valeur_basse):
        valeur_basse = temperature
    if(temperature > valeur_haute):
        valeur_haute = temperature
etendue = valeur_haute - valeur_basse
print("La valeur la plus petite est " + str(valeur_basse))
print("La valeur la plus haute est " + str(valeur_haute))
print("L'étendue des températures est " + str(etendue))