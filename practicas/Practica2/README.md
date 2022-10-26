# Práctica 2 - Algoritmos de Verificación

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

## Ejecutar scripts 🚀

*Los siguientes comandos ejecutaran el programa dependiendo la grafica que se desee consultar pueden ser ejecutados con **python** o **python3**.*

Abrir en su editor de texto favorito y ejetucar desde ahi o ejecutar en la terminal los siguientes comandos.

**Igual que la primer practica, para probar los valores de la grafica y verificar si ¿Existe una partición de G en 3 subconjuntos disjuntos tal que la subgráfica inducida de todos sea un clan?**

```bash
python clanes.py 'nombre de la grafica'
```

**Para generar un certificado aleatorio:**

```bash
python3 certificado.py 'nombre de la grafica' certificado.txt 
```

**Para ejecutar el algoritmo de verificación:**

```bash
python3 verificacion.py 'nombre de la grafica' certificado.txt
```

## 3 casos de prueba 🧪

### Ejemplar `graph_si.txt` con 6 vertices, 7 aristas, K=2

#### Certificado graph_si.txt

El siguiente comando `python3 certificado.py graph_si.txt certificado.txt` genera un certificado aleatorio o subconjunto de los vertices con un tamaño k guardandolo en un archivo tipo txt, para su mejor representacion se muestra por colores.

![Certificado](https://user-images.githubusercontent.com/41756950/197892790-0de31397-0084-4979-b8b5-8222458aff30.png)

#### Verificación `False` graph_si.txt

El siguiente comando `python3 verificacion.py graph_si.txt certificado.txt` ejecuta el algoritmo de verificació para el problema de PARTICIÓN DE CLANES, en su vesión de decisión.

En este caso **NO** satisface la condicion de pertenencia al lenguaje

![verificacion](https://user-images.githubusercontent.com/41756950/197894648-f829b1cd-919e-428f-90fa-d06ba70b4770.png)

#### Verificación `True` graph_si.txt

Volvemos   a ejecutar el comando `python3 verificacion.py graph_si.txt certificado.txt` pero esta vez con un certificado que si cumple con la condicion de pertenencia al lenguaje.

En este caso **SI** satisface la condicion de pertenencia al lenguaje

**Representacion gráfica:**

![grafica 1](https://cdn.discordapp.com/attachments/1009211692774866994/1018779425434767391/ejemplar2.png)

![Verificacion true](https://user-images.githubusercontent.com/41756950/197896053-c8bd594b-4aa5-410c-9878-6f8a3f584df4.png)

### Ejemplar `graph_si_3` con 6 vértices, 10 aristas, K=3

#### Certificado graph_si_3

El siguiente comando `python3 certificado.py graph_si_3.txt certificado.txt` genera un certificado aleatorio o subconjunto de los vertices con un tamaño k guardandolo en un archivo tipo txt, para su mejor representacion se muestra por colores.

![certificado](https://user-images.githubusercontent.com/41756950/197900630-6d5a7c58-e631-4729-b5b6-e37fc4367ed3.png)

#### Verificación `False` graph_si_3

El siguiente comando `python3 verificacion.py graph_si_3.txt certificado.txt` ejecuta el algoritmo de verificació para el problema de PARTICIÓN DE CLANES, en su vesión de decisión.

En este caso **NO** satisface la condicion de pertenencia al lenguaje

![verificacion false](https://user-images.githubusercontent.com/41756950/197900730-68c19184-e1ef-4bd9-a84e-03eb6ab88702.png)

#### Verificación `True` graph_si_3


Volvemos   a ejecutar el comando `python3 verificacion.py graph_si_3.txt certificado.txt` pero esta vez con un certificado que si cumple con la condicion de pertenencia al lenguaje.

En este caso **SI** satisface la condicion de pertenencia al lenguaje

**Representacion gráfica:**

![representacion grafica k=3](https://cdn.discordapp.com/attachments/1009211692774866994/1018776575312936970/ejemplar15.png)

![verificacion true](https://user-images.githubusercontent.com/41756950/197908407-f99ee887-09f8-420e-83e3-03bcbf6d525a.png)

### Ejemplar `graph_si_copy` con 6 vértices, 7 aristas, K=3

#### Certificado graph_si_copy

El siguiente comando `python3 certificado.py graph_si_copy.txt certificado.txt` genera un certificado aleatorio o subconjunto de los vertices con un tamaño k guardandolo en un archivo tipo txt, para su mejor representacion se muestra por colores.

![certificado](https://user-images.githubusercontent.com/41756950/197942639-c30ece5e-6486-4386-801d-e879b593b17a.png)

#### Verificación 1 `False` graph_si_copy

El siguiente comando `python3 verificacion.py graph_si_copy.txt certificado.txt` ejecuta el algoritmo de verificació para el problema de PARTICIÓN DE CLANES, en su vesión de decisión.

En este caso **NO** satisface la condicion de pertenencia al lenguaje

![Verificacion false](https://user-images.githubusercontent.com/41756950/197942692-c1785d73-d749-4d69-b5e5-e251bcd2a797.png)

#### Verificación  `True` graph_si_copy

El siguiente comando `python3 verificacion.py graph_si_copy.txt certificado.txt` ejecuta el algoritmo de verificació para el problema de PARTICIÓN DE CLANES, en su vesión de decisión.

En este caso **SI** satisface la condicion de pertenencia al lenguaje

**Representacion gráfica:**

![ejemplar](https://cdn.discordapp.com/attachments/1009211692774866994/1034697804985151488/draw.png)

![Verificacion true](https://user-images.githubusercontent.com/41756950/197939881-c6ac69dd-0f89-40e7-9bea-8937a9dffb13.png)

### Ejemplar `EXTRA` con 6 vértices, 6 aristas, K=2 que no es particion de clanes

#### Certificado extra graph_no.txt

Cualquier certificado generado no cumple con la condicion de pertenencia al lenguaje.


#### Verificación extra `False` graph_no.txt

El siguiente comando `python3 verificacion.py graph_no.txt certificado.txt` ejecuta el algoritmo de verificació para el problema de PARTICIÓN DE CLANES, en su vesión de decisión.

En este caso **NO** satisface la condicion de pertenencia al lenguaje

**Representacion gráfica:**

![representacion sin clanes](https://cdn.discordapp.com/attachments/1009211692774866994/1018787317214875648/ejemplar5.png)

![Error](https://user-images.githubusercontent.com/41756950/197938736-29b2ae32-79e0-461f-9773-80ce04277f93.png)

**Todos los ejemplares serán inválidos, ya que no cumple con la particion de clanes.**

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* 10/10 en la practica 2 🤓

---
⌨️ con ❤️ por  [VictorDeGallegos](https://github.com/VictorDeGallegos), [LuisHeragui](https://github.com/LuisHeragui) y [demian35](https://github.com/demian35)
