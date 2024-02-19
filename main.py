class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        tipoDisponible = ["electrico", "gasolina"]
        if tipo in tipoDisponible:
            self.tipo = tipo

class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        coloresDisponibles = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in coloresDisponibles:
            self.color = color

class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):
        cantidad = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                cantidad += 1
        return cantidad
    
    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if self.registro != asiento.registro:
                    return "Las piezas no son originales"
        return "Auto original"