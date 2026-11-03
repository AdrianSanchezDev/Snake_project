def crear_tablero_hardcodeado():
    tablero = [
        ["-","-","-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-","-","-"],
        ["-","o","-","-","-","-","0","-","-","-"],
        ["-","-","-","-","-","-","#","-","-","-"],
        ["-","-","-","-","#","#","#","-","-","-"],
        ["-","-","-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-","-","-"],
        ["-","-","-","-","-","-","-","-","o","-"],
        ["-","-","-","-","-","-","-","-","-","-"]
        ]
    return tablero
def dibujar_tablero(tablero):
    i = 0
    while i < len(tablero):
        for j in range(len(tablero[i])):
            print(tablero[i][j],end=" ")
        i = i + 1
        print("")
tableroD = crear_tablero_hardcodeado()
dibujar_tablero(tableroD)
#prueba
#def crear_tablero(dimL,dimA):
#    tablero = []
#    for 