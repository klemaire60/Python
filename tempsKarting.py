def saisie_valeurs() :
    groupe4 = []
    for i in range(3):
        valeur = float(input(f"entrer le temps N°{i + 1} "))
        groupe4.append(valeur)
        print(groupe4)
    return groupe4

tableau_temps = saisie_valeurs()

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

tableau_secondes = conversion_temps(tableau_temps)
print(str(meilleur_temps(tableau_secondes)) + " secondes est le meilleur temps")