# Práctica 1 - Esquemas de Codificación

[![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org) ![Status badge](https://img.shields.io/badge/status-%20terminado-green?style=for-the-badge)

## Complejidad Computacional, Universidad Nacional Autónoma de México semestre 2023-1

> ---
>
> * **Victor Hugo Gallegos Mota** - *316160456* - [VictorDeGallegos](https://github.com/VictorDeGallegos)
> * **José Demian Jiménez** - *314291707* - [demian35](https://github.com/demian35)
> * **Luis Alberto Hérnandez Aguilar** - *314208682* - [LuisHeragui](https://github.com/LuisHeragui)
>
>
>
> ---

## Pre-requisitos 📋

*Para poder ejecutar la aplicacion es necesario tener instalado python  con versiones superiores a la 3.9 en alguno de los siguientes enviroments.*

* Conda enviroment `conda 4.13.0`

```bash
python -V
Python 3.9.13
```

* Global enviroment `python3`

```bash
python3 -V
Python 3.10.6
```

## Ejecutar script 🚀

*Los siguientes comandos ejecutaran el programa dependiendo la grafica que se desee consultar pueden ser ejecutados con **python** o **python3**.*

Abrir en su editor de texto favorito y ejetucar desde ahi o ejecutar en la terminal los siguientes comandos.

```bash
python clanes.py graph_si.txt
```

```bash
python clanes.py graph_no.txt
```

```bash
python clanes.py graph_si_3.txt
```

## 3 casos de prueba solicitados 🧪

### Ejemplar con al menos 6 vértices, K=2, y con respuesta **SI**

Resultado en consola:

```bash
> python clanes.py graph_si.txt

Leyendo archivo...
101100101110011010011011100111010011101100111011110011110111001111011111001111011111100111110111100111110111111001111110111100111111011111

Numero de vértices en G: 6
Numero de aristas en G: 7
Valor de K: 2
Codificación del primer vértice de G: 1
Codificación de la primera arista: [1, 2]
¿Existe una partición de G en 2 subconjuntos disjuntos tal que la subgráfica inducida de ambos sea un clan? Sí
```

### Ejemplar con al menos 6 vértices, K=3, y con respuesta **SI**

Resultado en consola:

```bash
> python clanes.py graph_si_3.txt

Leyendo archivo...
10110010111111001101001101110011011111001101111110011101100111011110011101111100111011111100111101110011110111110011111011001111101110011111011110011111011111100111111010011111101100111111011100111111011111

Numero de vértices en G: 6
Numero de aristas en G: 10
k = 3
Codificación del primer vértice de G: 1
Codificación de la primera arista: [1, 2]
¿Existe una partición de G en 3 subconjuntos disjuntos tal que la subgráfica inducida de todos sea un clan? Sí
```

### Ejemplar con al menos 6 vértices, K=2, y con respuesta **NO**

Resultado en consola:

```bash
> python clanes.py graph_no.txt

Leyendo archivo...
101100101110011010011011111100111010011101111001111011100111101111100111110111100111111011

Numero de vértices en G: 6
Numero de aristas en G: 5
Valor de K: 2
Codificación del primer vértice de G: 1
Codificación de la primera arista: [1, 2]
¿Existe una partición de G en 2 subconjuntos disjuntos tal que la subgráfica inducida de ambos sea un clan? No
```

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* 10/10 en la practica 1 🤓

---
⌨️ con ❤️ por  [VictorDeGallegos](https://github.com/VictorDeGallegos), [LuisHeragui](https://github.com/LuisHeragui) y [demian35](https://github.com/demian35) 