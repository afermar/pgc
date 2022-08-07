import pandas as pd
import random as rand

pgc = pd.read_excel(r"~/pgc.xlsx", index_col=0)

pgc = pd.DataFrame(pgc)

pgc = list(pgc.to_dict().values()).pop()

pgc = {value:key for key, value in pgc.items()}

noms = list(pgc.keys())

def funcion():

    cuenta = rand.choice(noms)

    respuesta = input('¿Cuál es el número de esta cuenta?' + ' ' + cuenta + ' ')

    x = pgc.get(cuenta)

    if respuesta == str(x):
        print('¡Correcto!')
    else:
        print('Error, la respuesta correcta es:' + ' ' + str(x))

try:
    funcion()
    while True:
        funcion()

except KeyboardInterrupt:
    print("Aplicación detenida")

