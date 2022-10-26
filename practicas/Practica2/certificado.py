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
