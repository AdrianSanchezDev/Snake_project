def crear_mapa(filas, columnas):
    mapa = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("-")
        mapa.append(fila)
    return mapa

def crear_serpiente(filas, columnas):
    serpiente = [(1, 3), (2, 3), (3, 3)]
    
    
def main():
    filas=4
    columnas=4
    print(crear_mapa(filas, columnas))
    
main()
    