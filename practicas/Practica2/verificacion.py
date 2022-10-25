import sys
from curses.ascii import isdigit
from clanes import generarInfoGrafica

# Algoritmo que verifica el problema de partcion de clanes recibiendo como parametro el archivo graph_si.txt, el cual contiene la gráfica G y el archivo certificado.txt, el cual contiene la subgráfica certificada.

# El algoritmo tomara cada vértice de la sub grafica y buscara si en el conjunto de aristas original existe una arista que una a un vértice de esta subgrafica con algun otro de esta misma subgrafica. Si llegase a existir en alguna subgrafica una arista que una a dos vértices de la misma subgrafica el certificado sera rechaza, pues cada vértice perteneciente a una misma subgrafica tiene el mismo color, por lo cual no satisface el problema de coloracion de vértices. Si llegase a terminar la exploracién y ningun vértice es adyacente a otro de su misma subgrafica, el certificado se acepta, pues satisface al problema de coloracion de vértices.


def verificacion(k, aristas, certificado):
    if (len(certificado) > k):
        return False
    else:
        # Por cada subgráfica debemos de revisar que
        # para cada vértice exista una arista del vértice
        # a todos los demás de la misma.
        # Si no, entonces la subráfica no es un clan.
        for subgrafica in certificado:
            if len(subgrafica) > 1:
                for u in subgrafica:
                    for v in subgrafica:
                        if (u != v):
                            arista = [u, v]
                            if arista not in aristas:
                                return False
        return True


if __name__ == "__main__":

    print("\nLeyendo archivo...")
    f = open(sys.argv[1], "r")
    print(f.read())
    # Contar vértices del archivo sin duplciados.
    f = open(sys.argv[1], "r")

    certificado = []
    certificadoCadena = open(sys.argv[2], "r")
    certificadoCadena = certificadoCadena.read()
    certificadoCadena = certificadoCadena.split("\n")
    certificadoCadena = certificadoCadena[:-1]

    for s in certificadoCadena:
        verties = list(map(lambda x: int(x) if x.isdigit() else None, s))
        # quitar None
        verties = [i for i in verties if i is not None]
        certificado.append(verties)

    infoGrafica = generarInfoGrafica(f)
    graph = infoGrafica[0]
    vertices = infoGrafica[1]
    lista_aristas = infoGrafica[2]

    # Respuestas:
    print("\nNumero de vértices en G:", len(vertices))

    print("Numero de aristas en G:", int(len(lista_aristas)/2))

    # imprimir valor de k = 3 si el archivo leido es graph_si_3.txt
    if sys.argv[1] == "graph_si_3.txt":
        k = 3
        print("k = 3")
    elif sys.argv[1] == "graph_si.txt":
        k = 2
        print("k = 2")
    elif sys.argv[1] == "graph_no.txt":
        k = 2
        print("k = 2")

    print('Certificado: ', certificado)
    pregunta = "¿El ejemplar, con el certificado dado, satisface la condición de pertenencia al lenguaje correspondiente?"
    if verificacion(k, lista_aristas, certificado):
        print("{} Sí\n".format(pregunta))
    else:
        print("{} No\n".format(pregunta))
