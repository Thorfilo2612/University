"""Programa que calcula el volumen final de una arepa
El programa toma el volumen de los ingredientes
y calcula el volumen final que deberia tener la arepa"""

print("A continuación pondrás los ingredientes que lleva una arepa y su cantidad")

#Se declaran los ingredientes y los ingredientes se da en tazas excepto la sal, que se da en una cucharadita
ingrediente1 = input("¿Cuál es el primer ingrediente de una arepa?: ")
ingrediente2 = input("¿Cuál es el segundo ingrediente de una arepa?: ")
ingrediente3 = input("¿Cuál es el tercer ingrediente de una arepa?: ")

#Preparación de la mezcla
print("Tome en cuenta que la cantidad solo puede ser dada en números enteros, por el contrario se cerrara el programa")
preparacion1 = int(input("¿Cuántas tazas se le echa a la mezcla de harina?: "))
preparacion2 = int(input("¿Cuántas tazas se le echa a la mezcla de agua?: "))
preparacion3 = int(input("¿Cuántas cucharaditas se le echa a la mezcla de sal?: "))
print("Se mezclan el", ingrediente1, ",", ingrediente2, "y", ingrediente3, "en un bol")

#Final mezcla de la arepa
cantidad = preparacion1 + preparacion2 + preparacion3
print("La masa resultante es:", cantidad)
cerrar = input("Presione enter para cerrar")	
