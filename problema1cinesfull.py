FILAS = 5
ASIENTOS_POR_FILA = 10


def inicializar_sala():
 sala = []
 for i in range(FILAS):
    fila = [0] * ASIENTOS_POR_FILA
    sala.append(fila)
 return sala

def mostrar_sala(sala):
 print("\n--- Estado de la Sala ---")
 for f in range(FILAS):
    print(f"F{f+1}:", end=" ")
    for estado in sala[f]:
        simbolo = ""
        if estado == 0:
            simbolo = " D"
        elif estado == 1:
            simbolo = " V"
        elif estado == 2:
            simbolo = " R"
        print(simbolo, end="")
    print()

def validar_asiento(sala, fila, asiento):
 if fila >= 1 and fila <= 5 and asiento >= 1 and asiento <= 10:
    return 1
 else:
    return 0
 
def obtener_precio(fila):
 if fila == 1 or fila == 2:
    return 8000
 elif fila == 3 or fila == 4:
    return 6000
 elif fila == 5:
    return 4000
 return 0 
def vender_asiento(sala, fila, asiento):
 if validar_asiento(sala, fila, asiento) == 0:
    return 0
 
 indice_fila = fila - 1
 indice_asiento = asiento-1
 
 if sala[indice_fila][indice_asiento] == 0:
    sala[indice_fila][indice_asiento] = 1
    return obtener_precio(fila)
 else:
    return 0

def devolver_asiento(sala, fila, asiento):
 if validar_asiento(sala, fila, asiento) == 0:
    return 0
 indice_fila = fila - 1
 indice_asiento = asiento - 1
 precio_base = obtener_precio(fila)
 if sala[indice_fila][indice_asiento] == 1:
    sala[indice_fila][indice_asiento] = 2
    penalidad = precio_base * 0.20
    return penalidad

 elif sala[indice_fila][indice_asiento] == 2:
     sala[indice_fila][indice_asiento] = 0
     return -1
 
 else:
     return 0

def menu_principal():
 sala_cine = inicializar_sala()
 ingreso_neto = 0
 total_penalidades = 0
 opcion = 0
 
 while opcion != 4:
    print("\n==============================")
    print(" Menú: Cine Full ")
    print("================================")
    print("1. Venta de Asiento.")
    print("2. Recolección/Devolución de Asiento.")
    print("3. Mostrar Estado de la Sala.")
    print("4. Salir.")
 
    try:
     opcion = int(input("¿Cuál es su opción? "))
    except ValueError:
        print("Opción no válida.")
        continue
  
    if opcion == 1:
     print("\n--- VENTA DE ENTRADAS ---")
     try:
         f = int(input("Ingrese el número de Fila (1-5): "))
         a = int(input("Ingrese el número de Asiento (1-10): "))
    
     except ValueError:
        print("Fila o Asiento deben ser números.")
        continue
     precio_venta = vender_asiento(sala_cine, f, a)
    
     if precio_venta != 0: 
        ingreso_neto += precio_venta
        print(f"Venta exitosa. Asiento F{f}-A{a} vendido por  {precio_venta}")
     else:
            print(f"Error en la venta.")

    elif opcion == 2:
        print("\n--- RECOLECCIÓN/DEVOLUCIÓN ---")
        try:
            f = int(input("Ingrese el número de Fila (1-5): "))
            a = int(input("Ingrese el número de Asiento (1-10): "))
        except ValueError:
         print("Fila o Asiento deben ser números.")
         continue
    
        resultado = devolver_asiento(sala_cine, f, a)
    
        if resultado > 0:
            total_penalidades += resultado
            print(f"Devolución solicitada para F{f}-A{a}. Penalidad aplicada: {resultado}.")
        elif resultado == -1:
            precio_base = obtener_precio(f) 
            ingreso_neto -= precio_base
            print(f"Devolución completada para F{f}-A{a}.")
        else:
         print(f"El asiento F{f}-A{a} no se puede procesar.")
    
    elif opcion == 3:
        mostrar_sala(sala_cine)
    
    elif opcion == 4:
     print("\n--- RESUMEN DEL DÍA ---")
     print(f"Ingreso Total Neto: {ingreso_neto}")
     print(f"Total de Penalidades Acumuladas: {total_penalidades}")
     print("¡Gracias por usar el sistema Cine Full!")
    
    else:
     print("Opción no reconocida.")
if __name__ == "__main__":
    menu_principal()

#Analiza este código de Python del sistema Cine Full e identifica errores en la función inicializar_sala() y mostrar_sala(). Explica qué está mal y cómo corregirlo.
# por que el return sala no identifica la matriz sala?

# Revisa la funcion validar_asiento() y explica por qué no está funcionando correctamente. ¿Qué cambios se deben hacer para que valide correctamente los asientos?
# En la función validar_asiento(), el problema radica en la forma en que se están validando los parámetros de fila y asiento. Actualmente, la función está utilizando operadores lógicos incorrectos para verificar si los valores están dentro de los rangos permitidos. Para corregir esto, se deben utilizar operadores lógicos adecuados para validar que la fila esté entre 1 y 5, y que el asiento esté entre 1 y 10. La función corregida debería verse así:
# Analiza la función obtener_precio() y detecta errores lógicos en las condiciones if y elif. Explica cómo se pueden corregir para que la función devuelva el precio correcto según la fila.
# En la función obtener_precio(), el error lógico se encuentra en las condiciones if y elif. Actualmente, la función está utilizando operadores lógicos incorrectos para verificar las filas. Para corregir esto, se deben utilizar operadores lógicos adecuados para validar que la fila sea igual a 1 o 2, y que la fila sea igual a 3 o 4. La función corregida debería verse así:

#Revisa la función vender_asiento() y detecta errores relacionados con índices de listas y validación. Explica cómo se pueden corregir para que la función funcione correctamente.
# En la función vender_asiento(), el error relacionado con los índices de listas se encuentra en la forma en que se accede a los elementos de la matriz sala. Actualmente, la función está utilizando índices incorrectos para acceder a las filas y asientos. Para corregir esto, se deben ajustar los índices para que correspondan correctamente a las filas y asientos. La función corregida debería verse así:

#Analiza la función devolver_asiento() y revisa si existen errores en el manejo de índices, devoluciones y penalidades. Explica cómo se pueden corregir para que la función funcione correctamente.
# En la función devolver_asiento(), el error en el manejo de índices se encuentra en la forma en que se accede a los elementos de la matriz sala. Actualmente, la función está utilizando índices incorrectos para acceder a las filas y asientos. Para corregir esto, se deben ajustar los índices para que correspondan correctamente a las filas y asientos. Además, se debe asegurar que las penalidades se calculen correctamente según el precio base del asiento. La función corregida debería verse así:

#Revisa el menú principal del sistema Cine Full y detecta errores de sintaxis, impresión y cálculo del ingreso neto. Explica cómo se pueden corregir para que el menú funcione correctamente y muestre la información adecuada al usuario.
# En el menú principal del sistema Cine Full, se pueden detectar errores de sintaxis en la impresión de los mensajes y en la forma en que se calculan los ingresos netos. Para corregir esto, se deben revisar las cadenas de texto para asegurarse de que estén correctamente formateadas y que las variables se impriman de manera adecuada. Además, se debe asegurar que el cálculo del ingreso neto se realice correctamente al sumar los precios de venta y restar las penalidades. El menú corregido debería verse así:

#Analiza que error hace falta por corregir en el código para que el sistema funcione correctamente. Explica qué es lo que falta y cómo se puede implementar para completar el sistema Cine Full.
# Un error que falta por corregir en el código es la falta de manejo de excepciones en la entrada del usuario. Actualmente, el código no maneja adecuadamente los casos en los que el usuario ingresa valores no numéricos para las filas y asientos, lo que puede causar que el programa se bloquee. Para corregir esto, se pueden implementar bloques try-except para capturar las excepciones de tipo ValueError cuando el usuario ingresa datos no válidos. Esto permitirá que el programa continúe funcionando y le dará al usuario la oportunidad de ingresar datos correctos. La implementación podría verse así: