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
    
def comer(puntuacion, pos_comida, mapa, serpiente, cabeza_serpiente):
    if cabeza_serpiente == pos_comida:
        puntuacion = puntuacion + 1
        nueva_comida = crear_comida(mapa, serpiente, cabeza_serpiente)
        ultima_posicion = serpiente[len(serpiente) - 1]
        return nueva_comida, puntuacion, ultima_posicion
    return pos_comida, puntuacion, [-1,-1]

def crecer(ultima_posicion, puntuacion, serpiente, mapa):
    if ultima_posicion != [-1,-1]:
        serpiente.append(ultima_posicion)

def main():
    filas=10
    columnas=10
    puntuacion = 0
    ultima_posicion = [-1,-1]
    mapaD=crear_mapa(filas, columnas)
    dibujar_tablero(puntuacion, mapaD)
    serpiente, cabeza_serpiente=crear_serpiente(mapaD)
    pos_comida = crear_comida(mapaD, serpiente, cabeza_serpiente)
    mapa = dibujar_serpiente(puntuacion, serpiente,cabeza_serpiente,mapaD, pos_comida)
    
    dibujar_tablero(puntuacion, mapa)
    time.sleep(0.5)
    jugando = True
    while jugando:
        nueva_cabeza, nueva_posicion, jugando = movimiento_serpiente(mapaD, serpiente, cabeza_serpiente, jugando)
        nuevo_mapa = crear_mapa(filas, columnas)
        dibujar_tablero(puntuacion, nuevo_mapa)
        nuevo_mapa = dibujar_serpiente(puntuacion, nueva_posicion,nueva_cabeza,nuevo_mapa, pos_comida)
        crecer(ultima_posicion, puntuacion, serpiente, mapa)
        pos_comida, puntuacion, ultima_posicion = comer(puntuacion, pos_comida, nuevo_mapa, nueva_posicion, nueva_cabeza)    
        dibujar_tablero(puntuacion, nuevo_mapa)
        time.sleep(0.5)
        serpiente = nueva_posicion
    print("Has perdido.")
main()