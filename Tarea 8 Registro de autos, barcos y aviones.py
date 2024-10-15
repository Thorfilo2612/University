class Autos:
    seller = 'FlamaCar'
    def __init__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
    def show_attr(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Año: {self.año}"
    def __str__(self):
        return self.show_attr()
    
class Barcos:
    seller = 'FlamaBoat'
    def __init__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
    def show_attr(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Año: {self.año}"
    def __str__(self):
        return self.show_attr()
    
class Aviones:
    seller = 'FlamaPlane'
    def __init__(self, marca, modelo, color, año):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.año = año
    def show_attr(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}, Año: {self.año}"
    def __str__(self):
        return self.show_attr()
    
if __name__ == '__main__':
    Auto1 = Autos("Toyota", "Corolla", "Verde", 2008)
    Auto2 = Autos("Ford", "F150", "Rojo", 1950)
    Barco1 = Barcos("Fountaine Pajot", "Astrea 45", 2020, "Blanco")
    Barco2 = Barcos("SAS-Vektor", "SAS Adriana 44", 2012, "Blanco con negro")
    Avion1 = Aviones("BOMBARDIER", "LEARJET 75", 2019, "Bronze")
    Avion2 = Aviones("AIRBUS", "AIRBUS A330-200F", 2010, "Blanco con azul")

    print(Auto1)
    print(Auto2)
    print(Barco1)
    print(Barco2)
    print(Avion1)
    print(Avion2)
