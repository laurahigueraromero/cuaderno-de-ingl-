from cuaderno import Cuaderno
from conceptos import Conceptos


def menu_palabras(cuaderno):
    while True:
        print("\n-- Palabras --")
        print("1. Agregar palabra")
        print("2. Listar palabras")
        print("3. Eliminar palabra")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            word = input("Ingrese la palabra: ")
            translate = input("Ingrese la traducción: ")
            cuaderno.agregar_palabra(word, translate)
            print(f"Palabra '{word}' agregada con éxito.")
        elif opcion == "2":
            palabras = cuaderno.obtener_palabras()
            if palabras:
                print("\nPalabras en el cuaderno:")
                for palabra in palabras:
                    print(f"[{palabra[0]}] {palabra[1]} - {palabra[2]}")
            else:
                print("No hay palabras en el cuaderno.")
        elif opcion == "3":
            palabras = cuaderno.obtener_palabras()
            if palabras:
                print("\nPalabras en el cuaderno:")
                for palabra in palabras:
                    print(f"[{palabra[0]}] {palabra[1]} - {palabra[2]}")
                try:
                    id_del = int(input("Ingrese el ID de la palabra a eliminar: "))
                    cuaderno.eliminar_palabra(id_del)
                    print("Palabra eliminada con éxito.")
                except ValueError:
                    print("ID no válido.")
            else:
                print("No hay palabras en el cuaderno.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def menu_conceptos(conceptos):
    while True:
        print("\n-- Conceptos --")
        print("1. Agregar concepto")
        print("2. Listar conceptos")
        print("3. Eliminar concepto")
        print("4. Volver")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            concepto = input("Ingrese el concepto: ")
            definicion = input("Ingrese la definición: ")
            conceptos.agregar_concepto(concepto, definicion)
            print(f"Concepto '{concepto}' agregado con éxito.")
        elif opcion == "2":
            lista = conceptos.obtener_conceptos()
            if lista:
                print("\nConceptos guardados:")
                for c in lista:
                    print(f"[{c[0]}] {c[1]} - {c[2]}")
            else:
                print("No hay conceptos guardados.")
        elif opcion == "3":
            lista = conceptos.obtener_conceptos()
            if lista:
                print("\nConceptos guardados:")
                for c in lista:
                    print(f"[{c[0]}] {c[1]} - {c[2]}")
                try:
                    id_del = int(input("Ingrese el ID del concepto a eliminar: "))
                    conceptos.eliminar_concepto(id_del)
                    print("Concepto eliminado con éxito.")
                except ValueError:
                    print("ID no válido.")
            else:
                print("No hay conceptos guardados.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def main():
    cuaderno = Cuaderno()
    conceptos = Conceptos()

    while True:
        print("\nMenú principal:")
        print("1. Palabras")
        print("2. Conceptos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_palabras(cuaderno)
        elif opcion == "2":
            menu_conceptos(conceptos)
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
