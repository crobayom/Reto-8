# Reto-8

```

def x_elevado (*args) -> float:
    respuesta:float=1
    for i in args:
        if i==x:
            continue
        for j in i:
            respuesta*=x
        print (str(x)+" elevado a "+str(j)+" es: "+str(respuesta))
            
if __name__=="__main__":
    x:int=int(input("Ingrese el numero a elevar: "))
    a:int=int(input("Ingrese el numero que elevara primero a "+str(x)+": "))
    b:int=int(input("Ingrese el numero que elevara segundo a "+str(x)+": "))
    c:int=int(input("Ingrese el numero que elevara tercero a "+str(x)+": "))
    d:int=int(input("Ingrese el numero que elevara cuarto a "+str(x)+": "))
    e:int=int(input("Ingrese el numero que elevara quinto a "+str(x)+": "))
    x_elevado(x, a)
    x_elevado(x, a, b)
    x_elevado(x, a, b, c)
    x_elevado(x, a, b, c, d)
    x_elevado(x, a, b, c, d, e)
```
