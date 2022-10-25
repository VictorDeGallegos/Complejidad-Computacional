import sys
import random
from clanes import generarInfoGrafica

# Funcion para generar un certificado aleatorio.


def certificadoAleatorio(G):
    certificado = []
    vertices = []

    for i in G:
        vertices.append(i)
    # Desordenamos la lista de vértices para obtenerlos aleatoriamente.
    random.shuffle(vertices)

    while vertices:
        num_vertices = random.randint(1, len(vertices))
        s = []
        while num_vertices > 0:
            s.append(vertices.pop())
            num_vertices -= 1
        certificado.append(s)

    return certificado

# Algoritmo que verifica el problema de partcion de clanes recibiendo como parametro el archivo graph_si.txt, el cual contiene la gráfica G y el archivo certificado.txt, el cual contiene la subgráfica certificada.

# El algoritmo tomara cada vértice de la sub grafica y buscara si en el conjunto de aristas original existe una arista que una a un vértice de esta subgrafica con algun otro de esta misma subgrafica. Si llegase a existir en alguna subgrafica una arista que una a dos vértices de la misma subgrafica el certificado sera rechaza, pues cada vértice perteneciente a una misma subgrafica tiene el mismo color, por lo cual no satisface el problema de coloracion de vértices. Si llegase a terminar la exploracién y ningun vértice es adyacente a otro de su misma subgrafica, el certificado se acepta, pues satisface al problema de coloracion de vértices.


def verificacion():

    # Abrimos el archivo graph_si.txt y lo leemos
    archivo = open("graph_si.txt", "r")
    texto = archivo.read()
    archivo.close()

    # Creamos una lista con las lineas del archivo
    lineas = texto.split("\n")

    # Creamos un diccionario con la gráfica G
    G = dict()
    for i in range(1, len(lineas)):
        G[i] = dict()
        for j in range(1, len(lineas)):
            G[i][j] = int(lineas[i][j - 1])

    # Abrimos el archivo certificado.txt y lo leemos
    archivo = open("certificado.txt", "r")
    texto = archivo.read()
    archivo.close()

    # Creamos una lista con las lineas del archivo
    lineas = texto.split("\n")

    # Creamos un diccionario con la gráfica G
    C = dict()
    for i in range(1, len(lineas)):
        C[i] = dict()
        for j in range(1, len(lineas)):
            C[i][j] = int(lineas[i][j - 1])

    # Creamos una lista con los vertices de la subgrafica
    vertices = list(C.keys())

    # Creamos una lista con las aristas de la subgrafica
    aristas = []
    for i in C:
        for j in C:
            if (C[i][j] == 1):
                aristas.append((i, j))

    # Creamos una lista con los vertices de la gráfica original
    verticesG = list(G.keys())

    # Creamos una lista con las aristas de la gráfica original
    aristasG = []
    for i in G:
        for j in G:
            if (G[i][j] == 1):
                aristasG.append((i, j))

    # Revisamos si en la subgrafica existe una arista que una a un
    # vértice de esta subgrafica con algun otro de esta misma
    # subgrafica.
    for i in aristas:
        if (i[0] in vertices and i[1] in vertices):
            return False
            # print("Algoritmode verificacion: Rechazado")

    # Si no existe ninguna arista que una a un vértice de esta  subgrafica con algun otro de esta misma subgrafica, entonces el certificado es aceptado.
    return True
    # print("Algoritmo de verificacion: Aceptado")


if __name__ == "__main__":

    print("\nLeyendo archivo...")
    f = open(sys.argv[1], "r")
    print(f.read())
    # Contar vértices del archivo sin duplciados.
    f = open(sys.argv[1], "r")

    infoGrafica = generarInfoGrafica(f)
    graph = infoGrafica[0]

    # imprimir certificado aleatorio
    # certificadoAleatorio()
    certificado = certificadoAleatorio(graph)

    # Diccionario de colores para asignar un color diferente a cada indice de la lista para imprimirlo por color en la consola
    colores = ['\033[1;34;40m', '\033[1;31;40m', '\033[1;33;40m',
               '\033[1;32;40m', '\033[1;35;40m', '\033[1;36;40m']

    print("Un posible certificado es: ", end="")
    # Imprimir ceritificado con colores
    for i in range(len(certificado)):
        print(colores[i], certificado[i], end=" ")
    print()

    # Guardar certificado aleatorio en archivo
    archivo = open(sys.argv[2], "w")
    for i in certificado:
        archivo.write(str(i) + "\n")
    archivo.close()
