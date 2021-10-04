class Animales:
    vida = True
    muerte = True
    Dominio = "Eukaryota"
    Reino = "Animalia"

    def nacer(self):
        vida = "nacimiento"
    def morir(self):
        muerte = "fallecimiento"

Perro = Animales()
Perro.nacer()
