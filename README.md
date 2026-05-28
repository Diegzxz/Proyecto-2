# Calculadora en Python - Proyecto 2

Este programa es una calculadora hecha en Python que funciona directamente en la consola (la ventana negra de texto). No necesitas instalar nada especial, solo tener Python instalado en tu computadora.

---

## Requisitos

- Tener **Python 3** instalado. Si no lo tienes, puedes descargarlo desde https://www.python.org/downloads/
- No se necesitan librerias extras, todo el programa usa solo Python basico.

---

## Como ejecutar el programa

1. Descarga o clona este repositorio en tu computadora.
2. Abre una terminal o consola (en Windows puedes buscar "cmd" o "PowerShell" en el inicio).
3. Navega hasta la carpeta donde guardaste el archivo. Por ejemplo:
   ```
   cd C:\Users\TuNombre\Descargas\Proyecto-2
   ```
4. Ejecuta el programa con este comando:
   ```
   python "Proyecto 2.py"
   ```
5. Se mostrara el menu principal y podras empezar a usar la calculadora.

---

## Como usar el programa

Cuando el programa inicia, veras un menu con 6 opciones. Solo tienes que escribir el numero de la opcion que quieres y presionar **Enter**.

```
Menu de opciones
 1 - Operaciones Basicas
 2 - Operaciones Cientificas
 3 - Evaluacion de Funciones
 4 - Graficacion en Consola
 5 - Ver historial de aplicaciones
 6 - Salir de la Calculadora
```

---

### Opcion 1 - Operaciones Basicas

Aqui puedes hacer operaciones matematicas simples entre dos numeros:

| Opcion | Operacion       | Ejemplo               |
|--------|-----------------|-----------------------|
| 1      | Suma            | 5 + 3 = 8             |
| 2      | Resta           | 10 - 4 = 6            |
| 3      | Multiplicacion  | 6 * 7 = 42            |
| 4      | Division        | 15 / 3 = 5.0          |
| 5      | Potencia        | 2 elevado a 8 = 256   |

> **Importante:** Si intentas dividir entre 0, el programa te avisara con un error. Esto es normal, en matematicas no se puede dividir entre cero.

---

### Opcion 2 - Operaciones Cientificas

Aqui puedes hacer operaciones matematicas mas avanzadas con un solo numero:

| Opcion | Operacion                  | Ejemplo                        |
|--------|----------------------------|--------------------------------|
| 1      | Factorial                  | 5! = 120                       |
| 2      | Raiz Cuadrada              | Raiz de 16 = 4.00              |
| 3      | Exponencial (e^x)          | e^2 = 7.39 (aproximado)        |
| 4      | Seno (en radianes)         | Seno de 1.57 aprox 1.00        |
| 5      | Coseno (en radianes)       | Coseno de 0 = 1.00             |
| 6      | Logaritmo Natural (ln)     | ln(1) = 0.00                   |

> **Nota:** El seno y coseno usan **radianes**, no grados. Por ejemplo, 90 grados equivale a 1.5708 radianes.

---

### Opcion 3 - Evaluacion de Funciones

Aqui puedes calcular el resultado de una funcion matematica para un valor de X que tu eliges.

Las funciones disponibles son:
- **lineal** -> calcula `2x + 1`
- **cuadratica** -> calcula `x al cuadrado`
- **cubica** -> calcula `x al cubo`

**Ejemplo de uso:**
```
Elige una funcion (lineal, cuadratica, cubica): lineal
Ingresa el valor de x: 3
7
```
(Porque 2*3 + 1 = 7)

---

### Opcion 4 - Graficacion en Consola

Esta opcion muestra una grafica simple de la funcion elegida usando asteriscos (`*`) en la consola.

Elige entre: `lineal`, `cuadratica` o `cubica`.

El programa calculara los valores del 0 al 6 y mostrara cada punto como un `*` desplazado hacia la derecha segun el resultado.

> **Advertencia:** Si el valor de la funcion es muy grande (por ejemplo con la funcion cubica), los asteriscos se moveran mucho hacia la derecha y la grafica puede verse rara. Esto es normal.

---

### Opcion 5 - Ver historial

Muestra todas las operaciones que hiciste desde que abriste el programa, en orden. Si no has hecho ninguna operacion todavia, dira que el historial esta vacio.

---

### Opcion 6 - Salir

Cierra la calculadora. Al salir, el historial se borra porque el programa termina.

---

## Ejemplo de una sesion completa

```
Menu de opciones
 1 - Operaciones Basicas
 ...
Ingrese la opcion que desea ejecutar: 1

 1 - Suma
 ...
Ingrese la opcion que desea ejecutar: 1

Ingrese el Numero A a sumar: 10
Ingrese el Numero B a sumar: 5
El resultado es 15

Presione ENTER para volver al menu...
```

---

## Posibles errores comunes

| Error                                     | Causa                                         | Solucion                              |
|-------------------------------------------|-----------------------------------------------|---------------------------------------|
| `ERROR, no se puede dividir entre cero`   | Pusiste 0 como divisor                        | Elige otro numero como divisor        |
| `ERROR, solo ingrese numeros positivos`   | Pusiste un numero negativo en la raiz         | Ingresa un numero mayor o igual a 0   |
| `ERROR`                                   | Pusiste un numero negativo en el factorial    | Ingresa un numero entero positivo     |
| `La opcion X no es una opcion valida`     | Escribiste una opcion que no existe en el menu| Escribe solo los numeros que aparecen |
| `ERROR, el numero no puede ser menor a 0` | Pusiste 0 o negativo en el logaritmo         | Ingresa un numero mayor que 0         |
