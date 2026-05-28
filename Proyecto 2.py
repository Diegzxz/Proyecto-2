HistoryAll=[]

def lineal(x):
    return 2*x+1

def cuadratica(x):
    return x*x

def cubica(x):
    return x*x*x

#Funciones para mas tarde
def factorial(n):
    cont = 1

    for i in range(1, n + 1):
        cont *= i

    return cont

continuar_ejecutando = True
#Menu
while continuar_ejecutando:
    print("")
    print("Menu de opciones")
    print(" 1 - Operaciones Basicas")
    print(" 2 - Operaciones Cientificas")
    print(" 3 - Evaluacion de Funciones")
    print(" 4 - Graficacion en Consola")
    print(" 5 - Ver historial de aplicaciones")
    print(" 6 - Salir de la Calculadora")


    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True


#Opciones


    if opcion_elegida == "1":
        print(" 1 - Suma")
        print(" 2 - Resta")
        print(" 3 - Multiplicacion")
        print(" 4 - Division")
        print(" 5 - Potencia")
        opcion_basica = input("Ingrese la opcion que desea ejecutar: ").strip()

        if opcion_basica=="1":
            SumA=int(input("Ingrese el Numero A a sumar: "))
            SumB=int(input("Ingrese el Numero B a sumar: "))
            SumAB=SumA+SumB
            print(f'El resultado es {SumAB}')
            HistoryAll.append(f'Suma: {SumA} + {SumB} = {SumAB}')
        elif opcion_basica=="2":
            RestA=int(input("Ingrese el Numero A a restar: "))
            RestB=int(input("Ingrese el Numero B a restar: "))
            RestAB=RestA-RestB
            print(f'El resultado es {RestAB}')
            HistoryAll.append(f'Resta: {RestA} - {RestB} = {RestAB}')
        elif opcion_basica=="3":
            MultA=int(input("Ingrese el Numero A a multiplicar: "))
            MultB=int(input("Ingrese el Numero B a multiplicar: "))
            MultAB=MultA*MultB
            print(f'El resultado es {MultAB}')
            HistoryAll.append(f'Multiplicacion: {MultA} * {MultB} = {MultAB}')
        elif opcion_basica=="4":
            DivididA=int(input("Ingrese el Numero A a dividir: "))
            DivididB=int(input("Ingrese el Numero B a dividir: "))
            if DivididB==0:
                print("ERROR, no se puede dividir entre cero")
            else:
                DivididAB=DivididA/DivididB
                print(f'El resultado es {DivididAB}')
                HistoryAll.append(f'Division: {DivididA} / {DivididB} = {DivididAB}')
        elif opcion_basica=="5":
            PotenciA=int(input("Ingrese la base: "))
            PotenciB=int(input("Ingrese el exponente: "))
            PotenciAB=PotenciA**PotenciB
            print(f'El resultado es {PotenciAB}')
            HistoryAll.append(f'Potencia: {PotenciA} ** {PotenciB} = {PotenciAB}')

    elif opcion_elegida == "2":
        print(" 1 - Factorial")
        print(" 2 - Raiz Cuadrada")
        print(" 3 - Exponencial")
        print(" 4 - Seno")
        print(" 5 - Coseno")
        print(" 6 - Logaritmo Natural Aproximado")
        opcion_100 = input("Ingrese la opcion que desea ejecutar: ").strip()

        if opcion_100=="1":
            factou=int(input('Ingrese un numero: '))
            cont=1
            if factou<0:
                print('ERROR')
            else:
                for i in range(1,factou+1):
                    cont*=i
                print(f'El factorial es: {cont}')
                HistoryAll.append(f'Factorial: {factou}! = {cont}')
        elif opcion_100=="2":
            raiz2=int(input("Ingrese un numero para saber su raiz cuadrada: "))
            if raiz2<0:
                print("Error, solo ingrese numeros positivos")
            else:
                raiz3=raiz2**0.5
                print(f'La raiz cuadrada de {raiz2} es: {raiz3:.2f}')
                HistoryAll.append(f'Raiz Cuadrada: Raiz Cuadrada de {raiz2} = {raiz3:.2f}')
        elif opcion_100=="3":
            Expo=float(input("Ingrese el valor de x: "))
            das=0
            for i in range(20):
                das += (Expo**i)/factorial(i)
            print(f'La exponencial aproximada es: {das:.2f}')
            HistoryAll.append(f'Exponencial: e**{Expo} = {das:.2f}')
        elif opcion_100=="4":
            Sen=float(input("Ingrese el valor en radianes: "))
            asd=0
            for i in range(20):
                asd += ((-1)**i)*(Sen**(2*i+1))/factorial(2*i+1)
            print(f'El seno aproximado es: {asd:.2f}')
            HistoryAll.append(f'Seno: Seno de {Sen} = {asd:.2f}')
        elif opcion_100=="5":
            Cos=float(input("Ingrese el valor en radianes: "))
            dsa=0
            for i in range(20):
                dsa += ((-1)**i)*(Cos**(2*i))/factorial(2*i)
            print(f'El coseno aproximado es: {dsa:.2f}')
            HistoryAll.append(f'Coseno: Coseno de {Cos} = {dsa:.2f}')
        elif opcion_100=="6":
            In=float(input("Ingrese un numero mayor que 0: "))
            if In<=0:
                print("ERROR, el numero no puede ser menor a 0")
            else:
                y= (In-1)/(In+1)
                sad=0
                for i in range(20):
                    sad += (y**(2*i + 1)) / (2*i + 1)
                sad*=2
                print(f'El logaritmo natural aproximado es: {sad:.2f}')
                HistoryAll.append(f'Logaritmo Natural: LN de {In} = {sad:.2f}')
    elif opcion_elegida=="3":
        funcion=input("Elige una funcion (lineal, cuadratica, cubica): ").strip().lower()
        XX = int(input("Ingresa el valor de x: "))
        if funcion=="lineal":
            Yl=lineal(XX)
            print(Yl)
            HistoryAll.append(f'Funcion lineal: X={XX} Y={Yl}')

        elif funcion=="cuadratica":
            Yc=cuadratica(XX)
            print(Yc)
            HistoryAll.append(f'Funcion cuadratica: X={XX} Y={Yc}')

        elif funcion=="cubica":
            Ycc=cubica(XX)
            print(Ycc)
            HistoryAll.append(f'Funcion cubica: X={XX} Y={Ycc}')

        else:
            print("ERROR, elija una de esas tres funciones")

    elif opcion_elegida=="4":
        graff=input("Elige una funcion (lineal, cuadratica, cubica): ").strip().lower()

        if graff=="lineal" or graff=="cuadratica" or graff=="cubica":
            for i in range(7):
                if graff=="lineal":
                    grafy=lineal(i)
                elif graff=="cuadratica":
                    grafy=cuadratica(i)
                elif graff=="cubica":
                    grafy=cubica(i)
                print(" " * grafy + "*")

        else:
            print("ERROR, elija una de esas tres funciones")

    elif opcion_elegida=="5":
        print("")
        if len(HistoryAll) == 0:
            print("El historial esta vacio")
        else:
            print("Historial de operaciones:")
            for i in range(len(HistoryAll)):
                print(f"  {i + 1}. {HistoryAll[i]}")
    elif opcion_elegida == "6":
        continuar_ejecutando = False

    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")

    if continuar_ejecutando:
        input("Presione ENTER para volver al menu...")
