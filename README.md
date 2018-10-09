# Universidad Distrital Francisco José de Caldas

## Facultad Ingenieria

### Modelos de Programación II

#### Creador:

##### Cesar Alosno Llano Lagos - 20141020027
##### Jorge Antonio Escobar Bohorquez - 20152020120

#### Laberinto en Python:

##### El Siguiente programa se encarga de Resolver cualquier tipo de laberinto, siempre y cuando este elaborado con (1) y (0), siendo el (1) el obstaculo y (0) el camino por el cual se puede transitar.

##### Un ejemplo del Laberinto puede ser el siguiente.

Imagen del laberinto

##### Resuelve cualquier tipo de laberinto, este debe ser creado en un documento de texto, y ademas contener la posición inicial y la posición final (como se muestra en la siguiente imagen).

Imagen de las posiciones.

#### El Código:

##### Este metodo es el encargado de cargar los documentos de texto en donde se encuentra almacenado el laberinto a resolver, la posicion de inicio y la posicion final.

``` python
def cargarLaberinto(nombre):

    lector = open(nombre,"r")
    laberinto = lector.read().replace(',',' ').split('\n')
    return tuple([tuple(map(int, linea.split())) for linea in laberinto])
```

##### Estos metodos son la validacion de que el laberinto que queremos cargar y las coordenadas de inicio y fin esten bien coladas en el archivo de texto.


``` python
def comprobarValidezLaberinto(laberinto):
    if (len(laberinto)-2)>3 and len(laberinto[0])>3:
        return not(False in [len(laberinto[0])==len(linea) for linea in laberinto][:-2])
    return False

def comprobarValidezCoordenadas(laberinto):
    if laberinto[-1][0]<(len(laberinto)-2) and laberinto[-2][0]<(len(laberinto)-2):
        if laberinto[-1][1]<len(laberinto[0]) and laberinto[-2][1]<len(laberinto[0]):
            return True
    return False

```

##### Este metodo se encarga de comprobar que las coordenadas tanto de inicio como de fin, sean diferentes de (1), con ello nos encargamos de vericar que si exista una solucion (hasta el momento).

``` python

def comprobarLocalizacionCoordenadas(laberinto):
    return laberinto[laberinto[-1][0]][laberinto[-1][1]]!=1 and laberinto[laberinto[-2][0]][laberinto[-2][1]]!=1

```

##### En este metodo ya empezamos a hacer la validacion del posible camino que debemos recorrer para encontrar una solucion valida.
