from math import *
def clear_terminal():
    print("\n" * 10)

def resol_eq_second_degre(a,b,c):
    delta = b*b - 4 * a * c
    if(delta < 0):
        clear_terminal()
        print("Valeur de a : ",a ,"\nValeur de b : ",b ,"\nValeur de c : ",c ,"\n\nAucune solution réelle")
    elif (delta == 0):
        solution1 = b/2*a
        clear_terminal()
        print("Valeur de a : ",a ,"\nValeur de b : ",b ,"\nValeur de c : ",c ,"\n\nUne solution réelle possible \n x1 = " + str(solution1))
    else :
        solution1 = (-b - sqrt(delta)) / (2 * a)
        solution2 = (-b + sqrt(delta)) / (2 * a)
        clear_terminal()
        print("Valeur de a : ",a ,"\nValeur de b : ",b ,"\nValeur de c : ",c ,"\n\n2 solutions réelles possible : \nX1 = ", solution1, "\nx2 = ", solution2)

resol_eq_second_degre(
                     a = float(input("Entrer la valeur de A \n")),
                     b = float(input("Entrer la valeur de B \n")),
                     c = float(input("Entrer la valeur de C \n"))
                    )