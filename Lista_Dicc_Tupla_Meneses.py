# Desafío 1:
'''Escribir un programa que pregunte a diferentes personas cuánto conocen sobre contaminación del 1 al 10,
almacene estos valores en una lista y los muestre por pantalla ordenados de menor a mayor. '''
rta_contaminacion = []
continuar = True

while continuar:
    try:
        rta_persona = int(input("Del 1 al 10,\n¿Cuánto sabe de contaminación?\nIngrese un número para calificar.\nIngrese 0 para salir: \n"))
        
        if rta_persona == 0:
            print("Hasta luego.")
            continuar = False
        elif 1 <= rta_persona <= 10:
            rta_contaminacion.append(rta_persona)
        else:
            print("Ha ingresado un número incorrecto. Intente otra vez.\n")
    except ValueError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")

rta_contaminacion.sort()

print(f"La lista de respuestas de menor a mayor es: {rta_contaminacion}")

# Desafío 2:
'''Crea una tupla con los factores que más afectan a los mares.
Luego para jugar con niños y niñas, aprendiendo sobre contaminación del agua crea
un programa que pida números, si el numero esta entre 1 y la longitud máxima de la tupla,
muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero.'''

factores = ("MicroPlásticos", "Derrames de Petroleo", "Lixiviados Industriales", "Pesca Masiva", "Derretimiento de Casquetes Polares", "Liberación de Metano")
continuar = True

while continuar:
    try:
        posicion = int(input("Ingrese un número entero,\nSi el número corresponde a un índice de nuestra tupla,\nse mostrará el factor de contaminación guardado en esa posición.\nIngrese un número para calificar\nO ingrese 0 para salir: \n"))
        
        if posicion == 0:
            print("Hasta luego.")
            continuar = False
        elif 1 <= posicion:
            print(f"El factor obtenido es: {factores[posicion]}")
        else:
            print("Ha ingresado un número incorrecto. Intente otra vez.\n")
    except IndexError:
        print("NO. El número ingresado supera el máximo índice de la tupla. Intente otra vez.\n")
    except ValueError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")

# Desafío 3:
'''Crea un diccionario donde la clave sea el nombre de biólogos y el valor sea el email (no es necesario validar).
Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere insertar mas.
No se podrán insertar nombres repetidos.'''

biologos = {}
continuar = True

while continuar:
    print("Ingrese un nuevo contacto.")
    try:
        nombre=str(input("Nombre del biólogo: "))
        email=str(input("E-mail del biólogo: "))
        
        biologos[nombre]=email
        
        salir=str(input("Presione ENTER para continuar.\nPresione cualquier otra tecla para salir: "))

        if salir != "":
            continuar=False
        else:
            continue

    except ValueError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")

for key, value in biologos.items():
    print(f"Nombre del biólogo {key}: {key}\nCorreo electrónico: {value}\n")


# Desafío 4:
'''Escribir un programa que cargue una tupla con nombres de especie,
y para cada nombre de especie imprima el mensaje Hola soy ......, cuidame.'''

especies = list()
continuar = True

while continuar:
    print("Ingrese una nueva especie. Ingrese 0 y presione Enter para salir")
    try:
        especie_nueva=str(input("Nombre de la especie: "))
        
        if especie_nueva == "0":
            print("Hasta luego.")
            continuar = False
        else:
             especies.append(especie_nueva)
    except ValueError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")

especies_finalizado=tuple(especies)

for especie in especies_finalizado:
    print(f"Hola soy {especie}. Cuidame!")

# G1 Challenges  PARTE 1:
'''
Ejercicio 1:
Escribir un programa que solicite al usuario que ingrese asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
las almacene en una lista y al finalizar muestre por pantalla.
Defina que caracter o string hace que finalice la carga.
'''
# Coloque la resolución del Ejercicio debajo de esta línea
lista_asignaturas=[]
continuar=True

while continuar:
    try:
        asignatura = str(input("Ingrese una asignatura para guardar.\nPara salir ingrese 0: \n"))
        
        if asignatura == "0":
            print("Hasta luego.")
            continuar = False
        else:
            lista_asignaturas.append(asignatura)
    except ValueError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")

print(f"La lista de materias es: {lista_asignaturas}")

'''
Ejercicio 2:
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre 
por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada 
una de las asignaturas de la lista y <nota> cada una de las correspondientes notas 
introducidas por el usuario.
'''
# Coloque la resolución del Ejercicio debajo de esta línea

lista_asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
cont_asignaturas=0

while cont_asignaturas<len(lista_asignaturas):
    try:
        nota = int(input(f"Ingrese la nota correspondiente a {lista_asignaturas[cont_asignaturas]}: "))
        print(f"En {lista_asignaturas[cont_asignaturas]} ha sacado una nota igual a {nota}")
        cont_asignaturas += 1
    except ValueError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")


# G1 Challenges PARTE 2:
'''
Ejercicio 1:
Crea una tupla con los meses del año, pide números al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, 
muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero.
'''
# Coloque la resolución del Ejercicio debajo de esta línea
meses=("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
continuar = True

while continuar:
    try:
        numero = int(input("Ingrese un número distinto de cero: \nO ingrese 0 para salir: \n"))
        
        if numero == 0:
            print("Hasta luego.")
            continuar = False
        elif 1 <= numero <= len(meses):
            print(f"El mes obtenido es: {meses[numero-1]}")
        else:
            print("ERROR. El número ingresado no corresponde a ningún mes. Intente otra vez.\n")
    except IndexError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")
    except ValueError:
        print("Ha ingresado un dato incorrecto. Intente otra vez.\n")

'''
Ejercicio 2:
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
'''
# Coloque la resolución del Ejercicio debajo de esta línea

divisas={'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
continuar=True

while continuar:
    print("Divisas:\n1 para Euro\n2 para Dólar\n3 para Yen\n\n0 para salir.")
    try:
        opcion = int(input("Ingrese el número correspondiente a la divisa deseada y presione Enter: "))
        
        if opcion == 1:
            print(f"El símbolo correspondiente a Euros es €")
        elif opcion == 2:
            print(f"El símbolo correspondiente a Dollar es $")
        elif opcion == 3:
            print(f"El símbolo correspondiente a Yen es ¥")
        elif opcion == 0:
            print("Hasta luego.")
            continuar = False
        else:
            print("Ha ingresado una opción incorrecta. Intente otra vez.\n")
    
    except ValueError:
            print("Ha ingresado un dato incorrecto. Intente otra vez.\n")

'''
Ejercicio 3:
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla
        Fruta	    Precio
        Plátano	    1.35
        Manzana	    0.80
        Pera	    0.85
        Naranja	    0.70
y en otro diccionario simule una cesta de la compra. El programa debe preguntar el artículo 
y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
        Lista de la compra	 
        Artículo 1	        Precio
        Artículo 2	        Precio
        Artículo 3	        Precio
        …	…
        Total	            Coste.
'''
# Coloque la resolución del Ejercicio debajo de esta línea

frutas = {'Plátano':70, 'Manzana':80.5, 'Pera':85, 'Naranja':50}

carrito= {}
continuar = True

while continuar:
    print('Los productos disponibles son: Plátano, Manzana, Pera o Naranja')
    item = input('Introduzca nombre de producto: \n')

    if item in frutas:
        precio_fruta = float(frutas.get(item))
        print(f'{item} cuesta {precio_fruta} por Kg.')
        cantidad = float(input('Ingrese cantidad de Kg. \n'))
        precio_linea = precio_fruta * cantidad
        carrito[item] = precio_linea
    else:
        print('No se ha encontrado ese producto.')
    
    seguir = input('¿Quieres añadir artículos a la lista (Si/No)? ')
    if seguir=='No':
        continuar=False

costo_total = 0

print('Lista de compra')

for item, precio in carrito.items():
    print(item, '\t', precio)
    costo_total += precio
print('Costo total:', costo_total)