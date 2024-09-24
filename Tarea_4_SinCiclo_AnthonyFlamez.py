""" Calculo de años bisiestos sin ciclos. Gracias al calculo hecho, 
    pudimos concluir que hay 73 años bisiestos entre 1900 y 2199 """

print("Bienvenidos a esta calculadora de años bisiestos")
año = int(input("¿Coloque acá un año mayor a 1900 y menor a 2199: "))
if año <= 1900 or año >= 2199:
   print("Este año no es válido")
   quit()

# Acá confirmamos que el año puesto sea bisiesto o no
# Si el modulo da 0, quiere decir que es divisible entre 4, 100 y 400 el año que puso el usuario, por lo tanto es bisiesto

if año % 4 == 0:
  if año % 100 == 0:
    if año % 400 == 0:
      print("El año,", año, "es un año bisiesto")
    else:
      print ("El año", año, "no es un año bisiesto")
  else:
    print("El año", año, "es un año bisiesto")
else:
  print ("El año", año, "no es un año bisiesto")

# Colocamos el range en una lista, para así poder hacer las cuentas de manera automática  
añob = list(range(1900, año, 4))
añob.remove(1900)
if año >= 2100:
  añob.remove(2100)
# Solo 2100 y 1900 no son divisible entre 400, por lo tanto no son bisiestos
año_cuenta = len(añob)
print("Los años bisiestos entre 1900 y", año, "son:", año_cuenta)


# Nota: Añadi acá una confirmación de año bisiesto por hacer algo extra en esta tarea

