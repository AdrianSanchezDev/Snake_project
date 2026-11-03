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
    serpiente= [[5,1], [5,2]]
    cabeza_serpiente= [5,3]
    return serpiente, cabeza_serpiente
    
def movimiento_serpiente(mapa, serpiente, cabeza_serpiente):
    movimiento= input("usa W,A,S,D para mover la serpiente")
        if movimiento=="W":
            if cabeza_serpiente[0] != 0:
                cabeza_serpiente[0]= cabeza_serpiente[0]-1
        elif movimiento=="A":
            if cabeza_serpiente[1] != 0:
                cabeza_serpiente[1]= cabeza_serpiente[1]-1
        elif movimiento=="S":
            if cabeza_serpiente[0] != len(mapaD)
                cabeza_serpiente[0]= cabeza_serpiente[0]+1
        elif movimiento=="D":
            if cabeza serpiente[1] != len(mapaD[0])
                cabeza_serpiente[1]= cabeza_serpiente[1]+1

def main():
    filas=10
    columnas=10
    mapaD=crear_mapa(filas, columnas)
    dibujar_tablero(mapaD)
    serpiente, cabeza_serpiente=crear_serpiente(mapaD)
    movimiento_serpiente(mapa, serpiente, cabeza_serpiente)

main()

