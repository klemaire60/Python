from math import *
a = float(input("Entrer la valeur de A \n"))
b = float(input("Entrer la valeur de B \n"))
c = float(input("Entrer la valeur de C \n"))
delta = b*b - 4 * a * c
if(delta > 0):
    print("Aucune solution réelle")
elif (delta == 0):
    solution1 = b/2*a
    print("Une solution réelle possible \n x1 = " + str(solution1))
else :
    solution1 = (-b - sqrt(delta)) / (2 * a)
    solution2 = (-b + sqrt(delta)) / (2 * a)
    print("2 solutions réelles possible : \nX1 = %d\nx2 = %d", solution1, solution2)