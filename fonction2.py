def eq_fonction_affine(Xa,Ya,Xb,Yb) :
    if(Xa == Xb) :
        return print("Cette fonction est une constante")
    coef_dir = (Ya - Yb) / (Xa - Xb)
    ordo_origine = Ya - coef_dir * Xa

    if(coef_dir == 0) :
        fonction = "x + " + str(ordo_origine)
    elif(ordo_origine == 0) : 
        fonction = str(coef_dir) + " * x"
    else :
        fonction = str(coef_dir) + " * x + " + str(ordo_origine)
    print(fonction)

eq_fonction_affine(Ya = int(input("Entrez l'ordonnées du point A ")), Xa = int(input("Entrez l'absice du point A ")), Yb = int(input("Entrez l'ordonnées du point B ")), Xb = int(input("Entrez l'absice du point B ")))