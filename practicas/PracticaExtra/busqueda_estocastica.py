# Require
# MAX >= 1, total de iteraciones
# T >=0, temperatura inicial
# N : S -> 2^S, funcion de vecindad
# f : S -> R, funcion objetivo

# Ensure:
# s^* : S, solucion optima
# s<- Solucion aleatoria
#t<- 1
# while t <= MAX do
# s' <- N(s)
# if f(s') < f(s) then
# s <- s'
# else
# if random() < exp(-(f(s')-f(s))/t) then
# s <- s'
# end if
# t <- t + 1
# end while

import random
import sys
import math


def leer_instancia(archivo):  # Lee una instancia de un archivo
    instancia = {}  # Diccionario
    with open(archivo, 'r') as f:
        instancia['variables'] = int(f.readline())
        instancia['clausulas'] = int(f.readline())
        instancia['formula'] = []
        for _ in range(instancia['clausulas']):
            instancia['formula'].append([int(x) for x in f.readline().split()])
    return instancia


def leer_solucion(archivo):  # Lee una solucion de un archivo
    with open(archivo, 'r') as f:
        solucion = []
        line = f.readline()
        while line:
            solucion.append([int(x) for x in line.split()])
            line = f.readline()
    return solucion


def escribir_solucion(archivo, solucion):  # Escribe una solucion en un archivo
    with open(archivo, 'w') as f:
        for variable in solucion['asignacion']:
            f.write(str(variable[0]) + ' ' + str(variable[1]) + '\n')


def vecindad(asignacion, variables):  # Genera una vecindad de una asignacion
    # asignacion es una lista de 0 y 1
    # asignacion es la solucion actual
    # variables es una lista de variables
    # variables es la lista de variables
    # asignacion' es una lista de 0 y 1
    # asignacion' es una vecina de asignacion
    asignacion_ = asignacion.copy()  # Copia de asignacion
    i = random.randint(0, variables - 1)
    nuevo_valor = [asignacion[i][0], 1 - asignacion[i][1]]
    asignacion_[i] = nuevo_valor
    return asignacion_


def funcion_objetivo(instancia, asignacion):

    info = {}

    variables = instancia['variables']
    clausulas = instancia['clausulas']
    formula = instancia['formula']

    count = 0
    for clausula in formula:
        # [1,2,3] -> [1,1,0]
        if satisface(clausula, asignacion):
            count += 1

    info['variables'] = variables
    info['clausulas'] = clausulas
    info['clausulas_satisfacibles'] = count
    return info

# funcion auxiliar satisface()


def satisface(clausula, asignacion):
    for literal in clausula:
        for variable in asignacion:
            if literal == variable[0]:
                if variable[1] == 1:
                    return True
            elif literal == 0 - variable[0]:
                if variable[1] == 0:
                    return True
    return False


def busqueda_estocastica(instancia, solucion, T, iteraciones):

    nueva_solucion = {}
    nueva_solucion['asignacion'] = solucion

    # s es una lista de 0 y 1
    # s es la solucion actual
    s = solucion

    # t es un entero
    # t es el numero de iteracion actual
    t = 1

    while t <= iteraciones:
        s_ = vecindad(s, instancia['variables'])
        evaluacion_actual = funcion_objetivo(
            instancia, s)['clausulas_satisfacibles']
        evaluacion_nueva = funcion_objetivo(
            instancia, s_)['clausulas_satisfacibles']
        if evaluacion_nueva < evaluacion_actual:
            s = s_
            nueva_solucion['evaluacion'] = evaluacion_nueva
            nueva_solucion['asignacion'] = s
        else:
            if random.uniform(0, 1) <= math.exp(-(evaluacion_nueva - evaluacion_actual) / T):
                s = s_
                nueva_solucion['evaluacion'] = evaluacion_nueva
                nueva_solucion['asignacion'] = s
        t += 1

    return nueva_solucion


# Ejemplo de uso
if __name__ == "__main__":
    instancia = leer_instancia(sys.argv[1])
    solucion = leer_solucion(sys.argv[2])
    T = float(sys.argv[3])  # Temperatura inicial
    MAX = int(sys.argv[4])  # Numero de iteraciones

    print('Total de iteraciones:', MAX)
    print('F??rmula:', instancia['formula'])
    mejor_solucion = busqueda_estocastica(
        instancia, solucion, T, MAX)
    escribir_solucion(sys.argv[2], mejor_solucion)
    print('N??mero de cl??usulas:', instancia['clausulas'])
    print('N??mero de variables:', instancia['variables'])
    print('N??mero de cl??usulas que se satisfacen:',
          mejor_solucion['evaluacion'])
    print('Asignaci??n de verdad:', mejor_solucion['asignacion'])
