""" Calculo de años bisiestos con ciclos. Gracias al calculo hecho, 
    pudimos concluir que hay 73 años bisiestos entre 1900 y 2199 """

print("Bienvenidos a esta calculadora de años bisiestos")
año = int(input("¿Coloque acá un año mayor a 1900 y menor a 2199: "))
if año <= 1900 or año >= 2199:
   print("Este año no es válido")
   quit()

# A partir de acá haremos el cálculo de cuantos años bisiestos hay entre 1900 y los años propuestos por el usuario y removeremos 1900 y 2100 ya que no son años bisiestos
año_inicial = 1900
añob = list(range(1900, año, 4))
añob.remove(1900)
for i in añob:
   if año >= 2100:
      añob.remove(2100)
   cuenta = len(añob)
   print("Hay un total de", cuenta, "años bisiestos entre 1900 y", año)
   break
