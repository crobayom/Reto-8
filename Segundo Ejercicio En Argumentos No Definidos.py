
##*? No encontre ejercicios anteriores que estuvieran diseñados especificamente para esta situacion 
##*? y por tanto cambie un poco su funcionamiento, pero el proposito trate de mantenerlo, 
##*? esto manteniendo una eleccon de ejercicios retadores y relevantes

#*Numeros y su factorial, ejercicio 4 reto 7

#Importacion de funcion factorial para obviar el proceso de racionalizar su funcionamiento, 
#con un nombre especial para evitar conflictos con el nombre de la funcion que imprimira
from math import factorial as fact
#Definicion de la funcion que escribira los numeros y su factorial
def factorial(*args) ->int:
    for i in args:
        print(str(i)+" "+str(fact(i)))

if __name__=="__main__":
    a:int=int(input("Ingrese el primer numero a mostrar su factorial: "))
    b:int=int(input("Ingrese el segundo numero a mostrar su factorial: "))
    c:int=int(input("Ingrese el tercer numero a mostrar su factorial: "))
    d:int=int(input("Ingrese el cuarto numero a mostrar su factorial: "))
    e:int=int(input("Ingrese el quinto numero a mostrar su factorial: "))
    print("")
    factorial(a)
    print("")
    factorial(a, b)
    print("")
    factorial(a, b, c)
    print("")
    factorial(a, b, c, d)
    print("")
    factorial(a, b, c, d, e)
    print("")