cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]
costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
def cambiarValores():
    matriz = [ [10, 15, 20], [3, 7, 14] ]
    cantantes = [
        {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
        {"nombre": "Chayanne", "pais": "Puerto Rico"}
    ]

    ciudades = {
        "México": ["Ciudad de México", "Guadalajara", "Cancún"],
        "Chile": ["Santiago", "Concepción", "Viña del Mar"]
    }

    coordenadas = [
        {"latitud": 8.2588997, "longitud": -84.9399704}
    ]

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 3:
                matriz[i][j] = 6
    print (matriz)

    for i in cantantes:
        for key in i.keys():
            if i[key]=="Ricky Martin":
                i[key] = "Enrique Martin Morales"
    print(cantantes)

    for i in ciudades.keys():
        for j in range(len(ciudades[i])):
            if ciudades[i][j]=="Cancún":
                ciudades[i][j] = "Monterrey"
    print(ciudades)

    for i in range(len(coordenadas)):
        if coordenadas[i]['latitud']==8.2588997:
            coordenadas[i]['latitud'] = 9.9355431
    print(coordenadas)

def iterarDiccionario(lista):
    for i in range(len(lista)):
        for z,j in enumerate(lista[i].keys()):
            print(f'{j} - {lista[i][j]}{""if (z==len(lista[i].keys())-1) else ", " }',end="") #metodo bonus
        print("")
def iterarDiccionario2(key,lista):
    for i in range(len(lista)):
        print(lista[i][key])
def imprimirInformacion(diccionario):
    for y in diccionario.keys():
        print(f'{y.upper()}:{len(diccionario[y])}')
        for i in range(len(diccionario[y])):
            print(diccionario[y][i])
        print("")

cambiarValores()
iterarDiccionario(cantantes)
iterarDiccionario2('pais',cantantes)
imprimirInformacion(costa_rica)
