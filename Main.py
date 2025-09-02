#Main.py

#Tarea 2 Data Science

import pandas as pd
import os
from datos import datos

# Definimos las funciones para cada opción del menú
# Estas funciones son simuladas, tendrías que reemplazarlas con tu lógica real
def problema1():

    #Llama a la función de cálculo y muestra los resultados.
    
    resultados = calcular_analisis_notas()

    print("--- Resumen de Notas del Problema 1 ---")
    print(f"Promedio general del curso: {resultados['promedio_general']:.2f}")
    print("---")
    print(f"La nota más alta registrada es: {resultados['nota_mas_alta']:.2f}")
    print("---")
    print(f"La nota más baja registrada es: {resultados['nota_mas_baja']:.2f}")
    print("---")
    print(f"El alumno con el promedio más alto es: {resultados['alumno_promedio_max']['nombre']} con un promedio de {resultados['alumno_promedio_max']['promedio']:.2f}")
    print("---")
    print(f"El alumno con el promedio más bajo es: {resultados['alumno_promedio_min']['nombre']} con un promedio de {resultados['alumno_promedio_min']['promedio']:.2f}")
    print("\n--- DataFrame Completo con Promedios ---")
    print(resultados['df_completo'][['nombre', 'promedio']])

# Función principal que contiene el menú
def main():
    while True:
        # Limpiar la pantalla de la consola
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Menú del programa
        print("****************************************************************************************")
        print("\n-----Base de datos de Licencias Municipalidad de Pelotillehue-----\n")
        print("------------- MENU -------------")
        print("\n\u27a4 [1] Calcuar el promedio de noas y promedio mas alto y bajo.")
        print("\n\u27a4 [2] Filtrar estudiantes que aprobaron (promedio >= 4.0).")
        print("\n\u27a4 [3] Nota mas frecuente (moda) considerando todas las notas de todos los estudiantes.")
        print("\n\u27a4 [4] Porcentaje de estudiantes con al menos una nota bajo 4.0.")
        print("\n\u27a4 [5] Listado ordenado (de mayor a menor) de los estudiantes según su promedio.")
        print("\n\u27a4 [6] Terminar")
        print("\n****************************************************************************************")

        try:
            op = int(input("\nIngrese una opcion: "))
            
            if op < 1 or op > 6:
                print("\n*** Opcion invalida. Porfavor digite nuevamente ***\n")
                input("Presione Enter para continuar...")
                continue # Vuelve al inicio del bucle
            
            # Switch-case en Python (usamos un diccionario o if/elif/else)
            if op == 1:
                print("------------------------------------------------------------------------------------ ")
                print(" es:")
                problema1()  # Llamamos a la función del problema 1
                print("------------------------------------------------------------------------------------ ")
            
            elif op == 2:
                print("------------------------------------------------------------------------------------ ")
                print(" es:")
                #Ingresamos la funcion
                print("------------------------------------------------------------------------------------ ")
            elif op == 3:
                print("------------------------------------------------------------------------------------ ")
                print(" es:")
                #Ingresamos la funcion
                print("------------------------------------------------------------------------------------ ")
            elif op == 4:
                print("------------------------------------------------------------------------------------ ")
                print(" es:")
                #Ingresamos la funcion
                print("------------------------------------------------------------------------------------ ")
            
            elif op == 5:
                print("------------------------------------------------------------------------------------ ")
                print(" es:")
                #Ingresamos la funcion
                print("------------------------------------------------------------------------------------ ")
            
            elif op == 6:
                print("\n****Gracias por utilizar****")
                break

            while True:
                opcion = input("\n\u27a4¿Desea Realizar otra operacion? (Y=si/N=no): ").upper()
                if opcion == 'N':
                    print("\n****Gracias por utilizar****")
                    return
                elif opcion == 'Y':
                    break
                else:
                    print("Operacion invalida.")

        except ValueError:
            print("\n*** Opcion invalida. Porfavor digite un numero ***\n")
            input("Presione Enter para continuar...")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
