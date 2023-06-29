class Ave:
    def __init__(self) -> None:
        self.volador = True

    def vuela(self):
        print("vuela ave")

class Pato(Ave):
    def __init__(self) -> None:
        super().__init__()
        self.nada = False

    def vuela(self):
        super().vuela()
        print("vuela pato")

pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)