
from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import sumar_numeros

def menu():
    while True:
        print("\n--- Calculadora ---")
        print("1. Sumar dos números")
        print("2. Restar dos números")
        print("3. Multiplicar dos números")
        print("4. Dividir dos números")
        print("5. Suma avanzada (N números)")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {sumar(a, b)}")
        elif opcion == '2':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {restar(a, b)}")
        elif opcion == '3':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {multiplicar(a, b)}")
        elif opcion == '4':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print(f"Resultado: {dividir(a, b)}")
        elif opcion == '5':
            numeros = list(map(float, input("Ingrese los números separados por espacio: ").split()))
            print(f"Resultado: {sumar_numeros(numeros)}")
        elif opcion == '6':
            print("Gracias por usar la calculadora.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
