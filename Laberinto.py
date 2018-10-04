nombreArchivo = "TextoLaberinto.txt"

def cargarLaberinto(nombre):
    
    lector = open(nombre,"r")
    laberinto = lector.read().replace(' ','').replace(',','').split('\n')
    return tuple([tuple(map(int, linea)) for linea in laberinto])

def comprobarValidezLaberinto(laberinto):
    if (len(laberinto)-2)>3 and len(laberinto[0])>3:
        return not(False in [len(laberinto[0])==len(linea) for linea in laberinto][:-2])
    return False

def comprobarValidezCoordenadas(laberinto):
    if laberinto[-1][0]<(len(laberinto)-2) and laberinto[-2][0]<(len(laberinto)-2):
        if laberinto[-1][1]<len(laberinto[0]) and laberinto[-2][1]<len(laberinto[0]):
            return True
    return False

laberinto = cargarLaberinto(nombreArchivo)

print comprobarValidezCoordenadas(laberinto)