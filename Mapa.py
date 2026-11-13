import os
import time
import random

def crear_mapa(filas, columnas):
    mapa = []       
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("-")
        mapa.append(fila)
    
    return mapa

def dibujar_tablero(puntuacion, mapa):
    i = 0
    print(puntuacion)
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
            nueva_serpiente, pos_Final = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando, -1
    elif movimiento=="A":
        if cabeza_serpiente[1] != 0:
            cabeza_serpiente[1]= cabeza_serpiente[1]-1
            nueva_serpiente, pos_Final = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando, -1
    elif movimiento=="S":
        if cabeza_serpiente[0] != len(mapa) - 1:
            cabeza_serpiente[0]= cabeza_serpiente[0]+1
            nueva_serpiente, pos_Final = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando, -1
    elif movimiento=="D":
        if cabeza_serpiente[1] != len(mapa[0]) - 1:
            cabeza_serpiente[1]= cabeza_serpiente[1]+1
            nueva_serpiente, pos_Final = crear_nueva_serpiente(serpiente, cabeza_vieja)
        else:
            jugando = False
            return cabeza_serpiente, serpiente, jugando, -1
    return cabeza_serpiente, nueva_serpiente, jugando, pos_Final
def crear_nueva_serpiente(serpiente, cabeza_vieja):    
    nueva_serpiente = []
    nueva_serpiente.append(cabeza_vieja)
    for i in range(len(serpiente)-1):
        nueva_serpiente.append([serpiente[i][0],serpiente[i][1]])
    return nueva_serpiente, [serpiente[len(serpiente)-1][0], serpiente[len(serpiente)-1][1]]

def crear_comida(mapa, serpiente, cabeza_serpiente):
    posF_comida = random.randint(0,9)
    posC_comida = random.randint(0,9)
    pos_comida = [posF_comida, posC_comida]
    
    while (pos_comida[0] == cabeza_serpiente[0] and pos_comida[1] == cabeza_serpiente[1]) or pos_comida in serpiente:
        posF_comida = random.randint(0,9)
        posC_comida = random.randint(0,9)
        pos_comida = [posF_comida, posC_comida]
        
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == "M":
                return pos_comida
            
    mapa[posF_comida][posC_comida] = "M"
        
    return pos_comida

def dibujar_serpiente(puntuacion, serpiente, cabeza_serpiente, mapa, pos_comida):
    os.system("cls")
    dibujar_tablero(puntuacion, mapa)
    time.sleep(0.5)
    mapa[pos_comida[0]][pos_comida[1]] = "M"
    mapa[cabeza_serpiente[0]][cabeza_serpiente[1]] = "O"
    for i in range(len(serpiente)):
        mapa[serpiente[i][0]][serpiente[i][1]] = "#"
    os.system("cls")
    
    return mapa
    
def comer(puntuacion, pos_comida, mapa, serpiente, cabeza_serpiente, pos_Final):
    if cabeza_serpiente == pos_comida:
        puntuacion = puntuacion + 1
        nueva_comida = crear_comida(mapa, serpiente, cabeza_serpiente)
        crecer(pos_Final, puntuacion, serpiente, mapa)
        return nueva_comida, puntuacion
    return pos_comida, puntuacion

def crecer(pos_Final, puntuacion, serpiente, mapa):
    serpiente.append(pos_Final)
    
def colision(serpiente, cabeza_serpiente):
    for i in range(len(serpiente)):
        for j in range(len(serpiente)):
            if cabeza_serpiente == serpiente[i]:
                return False
    return True

def victoria(puntuacion):
    if puntuacion == 20:
        print("¡Victoria!")
        return False
    return True

def main():
    filas=10
    columnas=10
    puntuacion = 0
    mapaD=crear_mapa(filas, columnas)
    dibujar_tablero(puntuacion, mapaD)
    serpiente, cabeza_serpiente=crear_serpiente(mapaD)
    pos_comida = crear_comida(mapaD, serpiente, cabeza_serpiente)
    mapa = dibujar_serpiente(puntuacion, serpiente,cabeza_serpiente,mapaD, pos_comida)
    
    dibujar_tablero(puntuacion, mapa)
    time.sleep(0.5)
    jugando = True
    while jugando:
        jugando = victoria(puntuacion)
        if jugando == False:
            return -1
        nueva_cabeza, nueva_posicion, jugando, pos_Final = movimiento_serpiente(mapaD, serpiente, cabeza_serpiente, jugando)
        nuevo_mapa = crear_mapa(filas, columnas)
        dibujar_tablero(puntuacion, nuevo_mapa)
        nuevo_mapa = dibujar_serpiente(puntuacion, nueva_posicion,nueva_cabeza,nuevo_mapa, pos_comida)
        pos_comida, puntuacion = comer(puntuacion, pos_comida, nuevo_mapa, nueva_posicion, nueva_cabeza, pos_Final)    
        dibujar_tablero(puntuacion, nuevo_mapa)
        jugando = colision(nueva_posicion, nueva_cabeza)
        time.sleep(0.5)
        serpiente = nueva_posicion
    print("Has perdido.")
main()