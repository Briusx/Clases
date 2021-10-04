class Auto:
    llantas = 4
    puertas = 4
    Volante = True
    Asientos = 5
    motor = True
    Bolsa_de_aire = True

    def encender (self):
        motor = "encendido"
    def apagar (self):
        motor = "apagado"

Tesla = Auto()
Tesla.encender()
