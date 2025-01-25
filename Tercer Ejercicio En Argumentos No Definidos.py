
##*? No encontre ejercicios anteriores que estuvieran diseñados especificamente para esta situacion 
##*? y por tanto cambie un poco su funcionamiento, pero el proposito trate de mantenerlo, 
##*? esto manteniendo una eleccon de ejercicios retadores y relevantes


def x_elevado (*args) -> float:
    primero:bool=False
    for i in args:
        respuesta:float=1
        if primero==False:
            if i==x:
                primero=True
                continue
        for j in range(i):
            respuesta*=x
        print (str(x)+" elevado a "+str(i)+" es: "+str(respuesta))
            
if __name__=="__main__":
    x:int=int(input("Ingrese el numero a elevar: "))
    a:int=int(input("Ingrese el numero que elevara primero a "+str(x)+": "))
    b:int=int(input("Ingrese el numero que elevara segundo a "+str(x)+": "))
    c:int=int(input("Ingrese el numero que elevara tercero a "+str(x)+": "))
    d:int=int(input("Ingrese el numero que elevara cuarto a "+str(x)+": "))
    e:int=int(input("Ingrese el numero que elevara quinto a "+str(x)+": "))
    print("")
    x_elevado(x, a)
    print("")
    x_elevado(x, a, b)
    print("")
    x_elevado(x, a, b, c)
    print("")
    x_elevado(x, a, b, c, d)
    print("")
    x_elevado(x, a, b, c, d, e)
    print("")