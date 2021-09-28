
import time
import  random

biblioteca = {
    'global':
        [
         ['Stay(with Justin Bieber - The Kind LAROI, Justin Bieber)','F*ck LOVE 3:OVER YOU'] ,
         ['INDUSTRY BABY(feat.Jack Harlow) - Lil Nas X, Jack Harlow','INDUSTRY BABY'],
         ['Bad Habits - Ed Sheeran', 'Bad Habits'],
         ['Pepas - Farruko','Pepas'],
         ['Heat Waves - Glass Animals', 'Dreamland(+ Bonus Levels)'],
         ['Boulevard of broken dreams-green day', 'album2'],
         ['The day that never comes-metallica' ,'album 2'],
         ['Scorpions-wind of change' ,'album 1'],
         ['God only knows', 'pet sounds' ]
        ]
}


def listarCanciones():
    canciones = []
    for i, x in biblioteca['global']:
        cancion = i + x
        canciones.append(cancion)
    return canciones


def selectReproductor(cancion):
    print('-------------------------------------------------------------------')
    select_reproduccion = input('Seleccione la opcion \n a) Reproducir cancion  b) Reproducir todo   c)aleatorio:   ')

    if select_reproduccion == 'a':
        reproducirCancion(cancion)

    elif select_reproduccion == 'b':
        reproducirAll(cancion)
    elif select_reproduccion == 'c':
        reproducirRandom(cancion)

    else:
        return main()


def reproducirCancion(cancion):
    seleccion = int(input('Digite el numero de la cancion a reproducir: '))

    for i in range(len(cancion)):
        if seleccion  == i+1:
            reproducir(cancion[i])
    main()


def reproducirAll(cancion):
    for i in range(len(cancion)):
        reproducir(cancion[i])
    main()


def reproducirRandom(cancion):
    reproduccion = 0
    reproducida = []

    while reproduccion < len(cancion):
        canciones = random.choice(cancion)

        print(canciones)
        reproduccion+=1


def reproducir(cancion):
    print(f'Reproduciendo..... {cancion}')
    time.sleep(5)


def main():
    print('----------------Canciones mas escuchadas: Global-----------------')
    canciones = listarCanciones()
    for i in range(len(canciones)):
        print(i + 1, canciones[i])

    selectReproductor(canciones)

if __name__ == '__main__':
    main()