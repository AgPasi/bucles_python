# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio



while True:
    print("""
    1) Sumar                 3) Multiplicacion
    2) Restar                4) Division
    5) Exponente/Potencia
    """)
    opciones = input("Elige una opcion: ")

    primer_numero = int(input("Primer Numero: "))
    segundo_numero = int(input("Segundo Numero: "))

    if opciones == "1":
        print("-----------------Suma-----------------")
        suma = primer_numero + segundo_numero
        print("El resultado de la suma es: ", suma)

    if opciones == "2":
        print("-----------------Resta-----------------")
        resta = primer_numero - segundo_numero
        print("El resultado de la resta es: ", resta)

    if opciones == "3":
        print("-----------------Multiplicacion-----------------")
        multiplicacion = primer_numero * segundo_numero
        print("El resultado de la multiplicacion es: ", multiplicacion)

    if opciones == "4":
        print("-----------------Division-----------------")
        division = primer_numero / segundo_numero
        print("El resultado de la division es: ", division)

    if opciones == "5":
        print("-----------------Exponente/Potencia-----------------")
        exponente_potencia = primer_numero ** segundo_numero
        print("El resultado es: ", exponente_potencia)

    repeat = input("¿Deseas repetir? escribe (FIN) para salir: ").upper()
    if repeat == "FIN":
        break
    else:
        print("Error, caracter invalido")

print("El programa ha finalizado correctamente.")
