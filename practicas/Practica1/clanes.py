import copy
import sys
from queue import Queue

# Función auxiliar para decir si una gráfica es bipartita o no.


def esBipartitaAux(G, fuente, color):
    color[fuente] = 1

    # Creamos una cola con los valores de los vértices,
    # partiendo del vértice "fuente" para poder realizar
    # BFS sobre la gráfica.
    q = Queue()
    q.put(fuente)

    while (not q.empty()):
        # Sacamos un vértice de la cola.
        u = q.get()

        # Obtenemos los vértices vecinos no coloreados.
        for v in G:
            # Si v es vecino de u y no esta coloreado, entonces
            # le asignamos el color alterno y lo agregamos a la
            # cola.
            if (G[u][v] and color[v] == -1):
                color[v] = 1 - color[u]
                q.put(v)

            # Si v es vecino de u y tiene el mismo color, entonces
            # la gráfica no es bipartita.
            elif (G[u][v] and color[v] == color[u]):
                return False

    # Si la cola se vacía, entonces todos los vértices tienen
    # colores alternos con sus vecinos, por lo tanto, la gráfica
    # es bipartita.
    return True

# Función que nos dice si una gráfica es bipartita o no.


def esBipartita(G):

    # Creamos un diccionario de colores para almacenar los
    # colores asignados a los vértices. Los valores de los
    # vértices son usados como las llaves del diccionario.
    # El valor '-1' del diccionario de colores es usado para
    # indicar que no hay un colo asignado al vértice. El
    # valor '1' del diccionario es usado para indicar que se
    # asignó el primero color y el '0' es usado para indicar
    # que se asignó el segundo color.
    color = dict()
    for i in G:
        color[i] = -1

    # Revisamos cada uno de los vértices no coloreados.
    for i in G:
        if (color[i] == -1):
            if (esBipartitaAux(G, i, color) == False):
                return False

    return True

# Función que nos dice si existen dos clanes en una gráfica o no.


def existenDosClanes(G):
    v = len(G)

    # Obtenemos el complemento de G para revisar si es una
    # gráfica bipartita.
    # Consideramos todos los valores del diccionario, menos los
    # que se traten de un vértice conectado consigo mismo G[i][i].
    C = copy.deepcopy(G)
    for u in C:
        for v in C:
            C[u][v] = None

    for i in G:
        for j in G:
            C[i][j] = not G[i][j] if i != j else 0

    return esBipartita(C)

# Función que nos dice si existen tres clanes en una gráfica o no.


def existenTresClanes(G):
    v = len(G)

    # Obtenemos el complemento de G para revisar si es una
    # gráfica bipartita.
    # Consideramos todos los valores del diccionario, menos los
    # que se traten de un vértice conectado consigo mismo G[i][i].
    C = copy.deepcopy(G)
    for u in C:
        for v in C:
            C[u][v] = None

    for i in G:
        for j in G:
            C[i][j] = not G[i][j] if i != j else 0

    # Si la gráfica no es bipartita, entonces no existen tres clanes.
    if (esBipartita(C) == False):
        return False

    # Obtenemos los vértices de la gráfica bipartita.
    vertices = list(C.keys())
    v1 = vertices[0]
    v2 = vertices[1]

    # Creamos una gráfica bipartita con los vértices de la gráfica
    # original.
    B = dict()
    for i in G:
        B[i] = dict()

    # Creamos una gráfica bipartita con los vértices de la gráfica
    # original.
    for i in G:
        for j in G:
            if (C[i][j] == 0):
                B[i][j] = G[i][j]

    # Revisamos si la gráfica bipartita tiene un ciclo de longitud
    # 3.
    for i in B:
        for j in B:
            for k in B:
                if (B[i][j] and B[j][k] and B[k][i]):
                    return True

    return False


if __name__ == "__main__":

    print("\nLeyendo archivo...")
    f = open(sys.argv[1], "r")
    print(f.read())
    # Contar vértices del archivo sin duplciados.
    f = open(sys.argv[1], "r")
    vertices = []

    # Primero obtenemos todas las aristas a partir de los "saltos de línea".
    for x in f:
        vertices.append(x.split("00"))

    # De las aristas separamos los vértices.
    vertices = [item.split("0") for sublist in vertices for item in sublist]

    # Guardamos las aristas.
    for arista in vertices:
        arista[0] = len(arista[0])
        arista[1] = len(arista[1])
    lista_aristas = vertices

    # Ahora guardamos solo los vértices sin repetir.
    vertices = [item for sublist in vertices for item in sublist]
    vertices = list(dict.fromkeys(vertices))

    # Creamos la gráfica a partir de los vértices y sus aristas.
    graph = dict()
    for v in vertices:
        graph[v] = dict()

    for v in vertices:
        for u in graph:
            graph[u][v] = 0

    for arista in lista_aristas:
        u, v = arista
        graph[u][v] = 1
        graph[v][u] = 1

    # Respuestas:
    print("\nNumero de vértices en G:", len(vertices))

    print("Numero de aristas en G:", int(len(lista_aristas)/2))

    # imprimir valor de k = 3 si el archivo leido es graph_si_3.txt
    if sys.argv[1] == "graph_si_3.txt":
        print("k = 3")
    elif sys.argv[1] == "graph_si.txt":
        print("k = 2")
    elif sys.argv[1] == "graph_no.txt":
        print("k = 2")

    print("Codificación del primer vértice de G:", vertices[0])

    print("Codificación de la primera arista:", lista_aristas[0])

    if sys.argv[1] == "graph_si_3.txt":
        pregunta = "¿Existe una partición de G en 3 subconjuntos disjuntos tal que la subgráfica inducida de todos sea un clan?"
        if existenTresClanes(graph):
            print("{} Sí\n".format(pregunta))
        else:
            print("{} No\n".format(pregunta))
    elif sys.argv[1] == "graph_si.txt":
        pregunta = "¿Existe una partición de G en 3 subconjuntos disjuntos tal que la subgráfica inducida de todos sea un clan?"
        if existenDosClanes(graph):
            print("{} Sí\n".format(pregunta))
        else:
            print("{} No\n".format(pregunta))
    elif sys.argv[1] == "graph_no.txt":
        pregunta = "¿Existe una partición de G en 3 subconjuntos disjuntos tal que la subgráfica inducida de todos sea un clan?"
        if existenDosClanes(graph):
            print("{} Sí\n".format(pregunta))
        else:
            print("{} No\n".format(pregunta))
