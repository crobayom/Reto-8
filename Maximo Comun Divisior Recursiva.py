#def divisores (a:int, b:int) -> int:
 #   divisores:int=1
  #  respuesta:int=0
   # while divisores<=(a if a<b else b):
    #    if a % divisores == 0 and b % divisores == 0:
     #       respuesta=divisores
      #  divisores+=1
   # return respuesta
def divisores (a:int, b:int) -> int:
    respuesta:0
    for divisores in range(1, a+1 if a<b else b+1):
        if a % divisores == 0 and b % divisores == 0:
            respuesta=divisores
    return respuesta


def divisores_recursiva(a:int, b:int, c:int, respuesta:int) -> int:
    if c>(a if a<b else b):
        return respuesta
    elif a % c == 0 and b % c == 0:
        respuesta=c
        return divisores_recursiva(a, b, c+1, respuesta)
    else: 
            return divisores_recursiva(a, b, c+1, respuesta)




if __name__ == "__main__":
    respuesta:int=0
    a:int=int(input("Ingrese el priemer numero: "))
    b:int=int(input("Ingrese el segundo numero: "))
    c:int=1
    print("El mayor divisor entre "+str(a)+" y "+str(b)+" es "+str(divisores_recursiva(a,b,c,respuesta)))