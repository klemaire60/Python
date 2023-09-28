def saisie_valeurs() :
    groupe4 = []
    for i in range(3):
        valeur = float(input(f"entrer le temps N°{i + 1} "))
        groupe4.append(valeur)
    return groupe4

def conversion_temps(tableau_temps):
    tableau_secondes = []
    for minutes in tableau_temps:
        if minutes >= 1:
            secondes = round((minutes - 1) + 0.6, 2) * 100
        else:
            secondes = round(minutes, 2)
        tableau_secondes.append(secondes)
    return tableau_secondes

def meilleur_temps(tableau_secondes):
    for i in range(len(tableau_secondes)):
        temps = tableau_secondes[i]
        if i == 0 :
            meilleur_temps = temps
        elif  temps < meilleur_temps:
            meilleur_temps = temps
    return meilleur_temps

def print_minutes_secondes(meilleur_temps):
    minutes = meilleur_temps // 60
    secondes = meilleur_temps - 60
    print(f"Le meilleur temps est de {minutes} minute et {secondes} secondes.")

tableau_temps = saisie_valeurs()
tableau_secondes = conversion_temps(tableau_temps)
meilleur_temps = meilleur_temps(tableau_secondes)
print_minutes_secondes(meilleur_temps)