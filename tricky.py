import random

def DisplayBoard(tablero):
    tablero1=(("1-1","1"), ("1-2","2"), ("1-3","3"),
         ("2-1","4"), ("2-2","5"), ("2-3","6"),
         ("3-1","7"), ("3-2","8"), ("3-3","9"),   
         )

    tablerodict=dict(tablero1)
    lista=tablero
    valor=0

    if lista==[]:
        for num,dato in tablerodict.items():
            lista.append(dato)
 
    
    for x in range(4):
        print("+------+-"+"------+"+"------+")
        if x==3:
            break
        for i in range(4): 
            if i==2:
                print("|  ",lista[valor]," | ",lista[valor+1],"   | ",lista[valor+2],"  |")
                valor+=3
      
    return lista


def EnterMove(tablero):
    movimiento=False
    while movimiento != True:
        x=input("digita donde quieres poner tu movimiento")
        if x in tablero:
            x=int(x)
            x-=1
            tablero[x]='o'
            movimiento=True
        else:
            print("movimiento no valido")
            movimiento=False
    


def MakeListOfFreeFields(tablero):
    free=[]
    for i in range(len(tablero)):
        if tablero[i]!= "x" and tablero[i]!="o":   
                free.append(tablero[i])
        else:
                free.append(tablero[i])
   
    return free
   



def VictoryFor(tablero):    
    ganadorM=[["7","5","3"], ["1","5","9"],["4","5","6"],["2","5","8"]]
    ganadoresUoM=[["3","5","6"],["1","4","7"],["1","2","3"],["7","8","9"]] 
    i=0
    while i != 4:
        contador=0
        for x in range(3):
            y=ganadorM[i][x]
            y=int(y)
            if tablero[y-1] == 'x':
                contador+=1
            if contador==3:
                print("gano la Maquina")
                return 1
        i+=1         
    i=0
    while i != 4:
        contador=0
        for x in range(3):
            y=ganadoresUoM[i][x]
            y=int(y)
            if tablero[y-1] == 'x':
                contador+=1
            if contador==3:
                print("gano la Maquina")
                return 1
        i+=1
    i=0
    while i != 4:
        contador=0
        for x in range(3):
            y=ganadoresUoM[i][x]
            y=int(y)
            if tablero[y-1] == 'o':
                contador+=1   
            if contador==3:
                print("GANASTE")
                return 2
        i+=1
        
    

        

def DrawMove(tablero,movimientos):
    movimiento=False
    print("turno a la maquina")
    if movimientos==0:
        tablero[4]="x"

    while movimiento!= True:    
        while movimientos>0:
            x = random.randrange(9)+1   
            x= str(x)
            if x in tablero:           
                x=int(x)
                x-=1
                tablero[x]='x'
                movimiento=True
                movimientos-=movimientos
            else:
                movimiento=False
        DisplayBoard(tablero)
        return tablero
    

global movimientos
movimientos=0
ganador=False
tablero=[]
valor=0
while ganador != True:    
        tablero=DisplayBoard(tablero)
        tablero=DrawMove(tablero,movimientos)
        valor=VictoryFor(tablero)
        if valor==1:
            ganador=True
            tablero=DisplayBoard(tablero)
            break
            
        movimientos += 1
        tablero=MakeListOfFreeFields(tablero)
        EnterMove(tablero)
        movimientos+=1
        valor=VictoryFor(tablero)
        if valor==2:
            tablero=DisplayBoard(tablero)
            ganador=True
            break


    
