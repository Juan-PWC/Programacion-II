#1. crear clase vehiculo con: marca, modelo, linea :metodo: mostrar la info
#2. encapsulamiento. modificar vehiculo para velocidad sea privada
  #crear metodo para acelerar
#3. HERIENCIA. crear clase vehiculo, carro(hereda), moto(hereda) metoto: mostrar marca
#4. crear una lista con varios vehiculos y llamar metodo marca() en un for

class Vehiculo:
    def __init__(self, marca, modelo, linea):
        self.marca  = marca
        self.modelo = modelo
        self.linea  = linea
        self.__velocidad = 0

    def acelerar(self, incremento):
        self.__velocidad += incremento

    def mas_velocidad(self):
        return self.__velocidad

    def obtener_tipo(self):
        return "Vehiculo"

class Carro(Vehiculo):
    def obtener_tipo(self):
        return "Carro"

class Moto(Vehiculo):
    def obtener_tipo(self):
        return "Moto"

def mostrar_info(v):
    print(f"Tipo     : {v.obtener_tipo()}")
    print(f"Marca    : {v.marca}")
    print(f"Modelo   : {v.modelo}")
    print(f"Linea    : {v.linea}")
    print(f"Velocidad: {v.mas_velocidad()} km/h")
    print("-" * 30)

ve1 = Carro("Honda", "Civic", "Type R")
ve1.acelerar(80)

ve2 = Moto("Yamaha", "MT-07", "Sport")
ve2.acelerar(120)

ve3 = Carro("Mazda", "3", "Prime")
ve3.acelerar(60)

ve4 = Carro("MercedesBenz", "Clase c", "C200")
ve4.acelerar(110)

ve5 = Carro("BMW", "serie 3", "M340i")
ve5.acelerar(110)

ve6 = Carro("toyota", "Corolla", "SE")
ve6.acelerar(70)

ve7 = Carro("Ford", "Mustang", "GT")
ve7.acelerar(160)

ve8 = Moto("Honda", "CBR1000RR", "SP")
ve8.acelerar(120)

ve9 = Moto("BMW", "F900R", "Sport")
ve9.acelerar(120)

ve10 = Moto("Kawasaki", "Ninja", "ZX-10R")
ve10.acelerar(120)

vehiculos = [ve1, ve2, ve3, ve4, ve5, ve6, ve7, ve8, ve9, ve10]
for v in vehiculos:
    mostrar_info(v)
