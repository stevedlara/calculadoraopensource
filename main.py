import sumar
import restar
import multiplicar
import dividir
import suma_avanzada

def menu():
    while True:
        print("\nCalculadora:")
        print("1. Sumar 2 números")
        print("2. Restar 2 números")
        print("3. Multiplicar 2 números")
        print("4. Dividir 2 números")
        print("5. Sumar N números")
        print("6. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", sumar.sumar(a, b))

        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", restar.restar(a, b))

        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", multiplicar.multiplicar(a, b))

        elif opcion == "4":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", dividir.dividir(a, b))

        elif opcion == "5":
            numeros = input("Ingresa los números separados por comas: ").split(",")
            numeros = [float(num.strip()) for num in numeros]
            print("Resultado:", suma_avanzada.suma_avanzada(*numeros))

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()