nombreArchivo = "TextoLaberinto.txt"

def cargarLaberinto(nombre):
    
    lector = open(nombre,"r")
    laberinto = lector.read().replace(' ','').replace(',','').split('\n')
    return tuple([tuple(linea) for linea in laberinto])

laberinto = cargarLaberinto(nombreArchivo)

print laberinto