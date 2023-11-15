Ya = int(input("Entrez l'ordonnées du point A "))
Xa = int(input("Entrez l'absice du point A "))
Yb = int(input("Entrez l'ordonnées du point B "))
Xb = int(input("Entrez l'absice du point B ")) 

coef_dir = (Ya - Yb) / (Xa - Xb)
ordo_origine = Ya - coef_dir * Xa

fonction = str(coef_dir) + " * x + " + str(ordo_origine)
print(fonction)