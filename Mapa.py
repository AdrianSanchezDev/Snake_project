import os
import time

def crear_mapa(filas, columnas):
    mapa = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("-")
        mapa.append(fila)
    return mapa

def dibujar_tablero(mapa):
    i = 0
    while i < len(mapa):
        for j in range(len(mapa[i])):
            print(mapa[i][j],end=" ")
        i = i + 1
        print("")

def crear_serpiente(mapa):
    serpiente= [[5,2], [5,1]]
    cabeza_serpiente= [5,3]
    return serpiente, cabeza_serpiente
    
def movimiento_serpiente(mapa, serpiente, cabeza_serpiente, jugando):
    movimiento= input("usa W,A,S,D para mover la serpiente: ")
    cabeza_vieja = []
    cabeza_vieja.append(cabeza_serpiente[0])
    cabeza_vieja.append(cabeza_serpiente[1])
    if movimiento=="W":
        if cabeza_serpiente[0] != 0:
            cabeza_serpiente[0]= cabeza_serpiente[0]-1
            nueva_serpiente = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando
    elif movimiento=="A":
        if cabeza_serpiente[1] != 0:
            cabeza_serpiente[1]= cabeza_serpiente[1]-1
            nueva_serpiente = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando
    elif movimiento=="S":
        if cabeza_serpiente[0] != len(mapa) - 1:
            cabeza_serpiente[0]= cabeza_serpiente[0]+1
            nueva_serpiente = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando
    elif movimiento=="D":
        if cabeza_serpiente[1] != len(mapa[0]) - 1:
            cabeza_serpiente[1]= cabeza_serpiente[1]+1
            nueva_serpiente = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando
    return cabeza_serpiente, nueva_serpiente, jugando
def crear_nueva_serpiente(serpiente, cabeza_vieja):    
    nueva_serpiente = []
    nueva_serpiente.append(cabeza_vieja)
    for i in range(len(serpiente)-1):
        nueva_serpiente.append([serpiente[i][0],serpiente[i][1]])
    return nueva_serpiente

def dibujar_serpiente(serpiente, cabeza_serpiente, mapa):
    os.system("cls")
    dibujar_tablero(mapa)
    time.sleep(0.5)
    mapa[cabeza_serpiente[0]][cabeza_serpiente[1]] = "O"
    for i in range(len(serpiente)):
        mapa[serpiente[i][0]][serpiente[i][1]] = "#"
    os.system("cls")
    dibujar_tablero(mapa)
    time.sleep(0.5)
    
def main():
    filas=10
    columnas=10
    mapaD=crear_mapa(filas, columnas)
    dibujar_tablero(mapaD)
    serpiente, cabeza_serpiente=crear_serpiente(mapaD)
    dibujar_serpiente(serpiente,cabeza_serpiente,mapaD)
    jugando = True
    while jugando:
        nueva_cabeza, nueva_posicion, jugando = movimiento_serpiente(mapaD, serpiente, cabeza_serpiente, jugando)
        nuevo_mapa = crear_mapa(filas, columnas)
        dibujar_tablero(nuevo_mapa)
        dibujar_serpiente(nueva_posicion,nueva_cabeza,nuevo_mapa)
        serpiente = nueva_posicion
    print("Has perdido.")
main()