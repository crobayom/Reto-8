#Definicion de la funcion que devolvera un numero potenciado a otro
def potencia (x:float, y:int, respuesta:float) -> float:
    #Condicional que ejemplifica el caso base de la forma recursiva de las funciones, en este caso devuelve 1 porque elevar un numero a 0 es 1
    if y==0: return 1
    #En caso de que el numero que eleva aun no haya bajado lo suficiente (por la propiedad recursiva), se devolvera a la potencia 
    return respuesta*potencia(x,y-1,respuesta)

if __name__=="__main__":
    x:float=float(input("Ingrese el numero a elevar: "))
    respuesta:float=x
    y:int=int(input("Ingrese el numero que elevara a "+str(x)+": "))
    print(potencia(x, y, respuesta))