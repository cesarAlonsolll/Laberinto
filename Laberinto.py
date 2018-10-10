nombreArchivo = "TextoLaberinto.txt"

def cargarLaberinto(nombre):
    lector = open(nombre,"r")
    laberinto = lector.read().replace(',',' ').split('\n')
    return tuple([tuple(map(int, linea.split())) for linea in laberinto])

def comprobarValidezLaberinto(laberinto):
    if (len(laberinto)-2)>3 and len(laberinto[0])>3:
        return not(False in [len(laberinto[0])==len(linea) for linea in laberinto][:-2])
    return False

def comprobarValidezCoordenadas(laberinto):
    if laberinto[-1][0]<(len(laberinto)-2) and laberinto[-2][0]<(len(laberinto)-2):
        if laberinto[-1][1]<len(laberinto[0]) and laberinto[-2][1]<len(laberinto[0]):
            return True
    return False

def comprobarLocalizacionCoordenadas(laberinto):
    return laberinto[laberinto[-1][0]][laberinto[-1][1]]!=1 and laberinto[laberinto[-2][0]][laberinto[-2][1]]!=1

def comprobarExistenciaRuta(laberinto):
    if (comprobarValidezLaberinto(laberinto) and comprobarValidezCoordenadas(laberinto)
        and comprobarLocalizacionCoordenadas(laberinto)):
        
        def comprobarDestino(coordenadasA, coordenadasF):
            return coordenadasA==coordenadasF
        
        def comprobarCamino(coordenadasA, coordenadasF, y, x):
            return laberinto[coordenadasA[0]+y][coordenadasA[1]+x]==0
        
        def iniciar(coordenadasA, coordenadasF):
            if comprobarDestino(coordenadasA, coordenadasF):
                return True
            if comprobarCamino(coordenadasA, coordenadasF, -1, 0):
                return avanzar( (coordenadasA[0]-1,coordenadasA[1]), coordenadasF, [coordenadasA],
                               ((-1, 0), (0, 1), (0, -1)))
            if comprobarCamino(coordenadasA, coordenadasF, 0, 1):
                return avanzar( (coordenadasA[0],coordenadasA[1]+1), coordenadasF, [coordenadasA],
                               ((0, 1), (1, 0), (-1, 0)))
            if comprobarCamino(coordenadasA, coordenadasF, 1, 0):
                return avanzar( (coordenadasA[0]+1,coordenadasA[1]), coordenadasF, [coordenadasA],
                               ((1, 0), (0, -1), (0, 1)))
            if comprobarCamino(coordenadasA, coordenadasF, 0, -1):
                return avanzar( (coordenadasA[0],coordenadasA[1]-1), coordenadasF, [coordenadasA],
                               ((0, -1), (-1, 0), (1, 0)))
            return False
        
        def avanzar(coordenadasA, coordenadasF, visitadas, orden):
            if coordenadasA in visitadas:
                return False
            if comprobarDestino(coordenadasA, coordenadasF):
                return True
            if comprobarCamino(coordenadasA, coordenadasF, *orden[0]):
                if avanzar( (coordenadasA[0]+orden[0][0],coordenadasA[1]+orden[0][1]), coordenadasF, visitadas+[coordenadasA],
                           orden):
                    return True
            if comprobarCamino(coordenadasA, coordenadasF, *orden[1]):
                if avanzar( (coordenadasA[0]+orden[1][0],coordenadasA[1]+orden[1][1]), coordenadasF, visitadas+[coordenadasA],
                           ((orden[0][1],-orden[0][0]), (orden[1][1],-orden[1][0]), (orden[2][1],-orden[2][0]))):
                    return True
            if comprobarCamino(coordenadasA, coordenadasF, *orden[2]):
                if avanzar( (coordenadasA[0]+orden[2][0],coordenadasA[1]+orden[2][1]), coordenadasF, visitadas+[coordenadasA],
                           ((-orden[0][1],orden[0][0]), (-orden[1][1],orden[1][0]), (-orden[2][1],orden[2][0]))):
                    return True
            return False
        
        return iniciar(laberinto[-2], laberinto[-1])
        
    return False

laberinto = cargarLaberinto(nombreArchivo)

print comprobarExistenciaRuta(laberinto)