def eq_fonction_affine(Xa,Ya,Xb,Yb) :

    coef_dir = (Ya - Yb) / (Xa - Xb)
    ordo_origine = Ya - coef_dir * Xa

    fonction = str(coef_dir) + " * x + " + str(ordo_origine)
    print(fonction)

eq_fonction_affine(Ya = float(input("Entrez l'ordonnées du point A ")), Xa = float(input("Entrez l'absice du point A ")), Yb = float(input("Entrez l'ordonnées du point B ")), Xb = float(input("Entrez l'absice du point B ")))