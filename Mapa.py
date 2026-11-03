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

def main():
    filas=10
    columnas=10
    mapaD=crear_mapa(filas, columnas)
    dibujar_tablero(mapaD)
main()