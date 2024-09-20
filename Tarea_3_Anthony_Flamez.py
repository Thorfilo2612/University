# Inicio del camino de un entrenador pokemon

print("Bienvenido a la región de Johto")
print("Soy el profesor Oak")

# Acá definiremos la edad del entrenador
edad = int(input("¿Qué edad tienes(solo en números enteros)?: "))
if edad > 10 and edad < 110:
  print("¡Tu aventura comienza ya!")
else:
  print("No tienes edad para ser entrenador(a)")
  input("Debes reiniciar el programa")
  quit()

# Acá definiremos el sexo del entrenador
genero = input("¿Eres un chico o una chica?: ")
if  genero == "chico":
  print("¡Bienvenido!")
elif genero == "chica":
    print("¡Bienvenida!")
else:
    print("Debes decir chico o chica")
    input("Debes reiniciar el programa")
    quit()

# A partir de acá habrá un if con un else, uno por si el genero es chico o si es chica, pero empezaremos por chicos
if genero == "chico":
  # Acá definiremos de que región es el entrenador
  print("En este mundo solo existen Kanto, Johto, Hoenn, Sinnoh, Teselia, Kalos, Alola, Galar y Paldea")
  reg = input("¿De que región vienes?: ")

  # Acá definiremos el compañero del entrenador
  print("Necesitaras un compañero de viaje")
  print("Como eres un chico, ¡Tu compañera de viaje es Misty!")
  comp_jugador = "Misty"

  # Acá definiremos el tipo de pokemon y su pokemon inicial del entrenador
  print("Los pokemones iniciales son de tipo agua, fuego y planta") 
  tipo_pokemon = input("¿Qué tipo de pokemon quieres para empezar?: ")
  if tipo_pokemon == "agua":  
    print("Tu starter es Piplup")
    pokemon = "Piplup"
  elif tipo_pokemon == "fuego":
    print("Tu starter es Cyndaquill")
    pokemon = "Cyndaquill"
  elif tipo_pokemon == "planta":
    print("Tu starter es Turtwig")
    pokemon = "Turtwig"
  else:
    print("Debes escoger agua, fuego o planta")
    input("Debes reiniciar el programa")
    quit()

  print("Excelente entrenador, tienes la edad de", edad, "años, vienes de la región de", reg, ", tu pokemon inicial es", pokemon, "y tu compañera de viaje es", comp_jugador)
  input("Presiona enter para cerrar")
# A partir de acá funciona si es para las chicas
else:
  # Acá definiremos de que región es el entrenador
  print("En este mundo solo existen Kanto, Johto, Hoenn, Sinnoh, Teselia, Kalos, Alola, Galar y Paldea")
  reg = input("¿De que región vienes?: ")

  # Acá definiremos el compañero del entrenador
  print("Necesitaras un compañero de viaje")
  print("Como eres chica, ¡Tu compañero de viaje es Brook!")
  comp_jugador = "Brook"

  # Acá definiremos el tipo de pokemon y su pokemon inicial del entrenador
  print("Los pokemones iniciales son de tipo agua, fuego y planta") 
  tipo_pokemon = input("¿Qué tipo de pokemon quieres para empezar?: ")
  if tipo_pokemon == "agua":
    print("Tu starter es Piplup")
    pokemon = "Piplup"
  elif tipo_pokemon == "fuego":
    print("Tu starter es Cyndaquill")
    pokemon = "Cyndaquill"
  elif tipo_pokemon == "planta":
    print("Tu starter es Turtwig")
    pokemon = "Turtwig"
  else:
    print("Debes escoger agua, fuego o planta")
    input("Debes reiniciar el programa")
    quit()

  print("Excelente entrenadora, tienes la edad de", edad, "años , vienes de la región de", reg, ", tu pokemon inicial es", pokemon, "y tu compañero de viaje es", comp_jugador)
  input("Presiona enter para cerrar")

