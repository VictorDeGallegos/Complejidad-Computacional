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


def leer_instancia(archivo):
    instancia = {}  # Diccionario
    with open(archivo, 'r') as f:
        instancia['variables'] = int(f.readline())
        instancia['clausulas'] = int(f.readline())
        instancia['formula'] = []
        for _ in range(instancia['clausulas']):
            instancia['formula'].append([int(x) for x in f.readline().split()])
    return instancia


def leer_solucion(archivo):
    solucion = {}
    with open(archivo, 'r') as f:
        solucion['evaluacion'] = int(f.readline())
        solucion['asignacion'] = []
        line = f.readline()
        while line:
            solucion['asignacion'].append([int(x) for x in line.split()])
            line = f.readline()
    return solucion


def escribir_solucion(archivo, solucion):
    with open(archivo, 'w') as f:
        f.write(str(solucion['evaluacion']) + '\n')
        for variable in solucion['asignacion']:
            f.write(str(variable[0]) + ' ' + str(variable[1]) + '\n')


def vecindad(asignacion, variables):
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


def funcion_objetivo(instancia, solucion):

    info = {}

    instancia = leer_instancia(instancia)  # Instancia
    solucion = leer_solucion(solucion)  # Solucion inicial

    print('Fórmula:', instancia['formula'])
    formula = instancia['formula']
    asignacion = solucion['asignacion']

    info['clausulas'] = instancia['clausulas']
    info['variables'] = instancia['variables']

    count = 0
    for clausula in formula:
        # [1,2,3] -> [1,1,0]
        if satisface(clausula, asignacion):
            count += 1

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

    nueva_solucion = solucion

    # s es una lista de 0 y 1
    # s es la solucion actual
    s = funcion_objetivo(instancia, solucion)

    # t es un entero
    # t es el numero de iteracion actual
    t = 1

    while t <= iteraciones:
        s_ = vecindad(s, instancia['variables'])
        evaluacion_actual = funcion_objetivo(instancia['formula'], s)
        evaluacion_nueva = funcion_objetivo(instancia['formula'], s_)
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

    instancia = sys.argv[1]
    solucion = sys.argv[2]
    T = float(sys.argv[3])  # Temperatura inicial
    MAX = int(sys.argv[4])  # Numero de iteraciones

    mejor_solucion = busqueda_estocastica(
        instancia, solucion, T, MAX)
    escribir_solucion(sys.argv[2], mejor_solucion)
    print('Mejor solución:', mejor_solucion)
