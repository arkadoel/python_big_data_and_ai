lista = list(range(1,4,1))

print(lista)
lista.append(4)

'''queremos personalizar y tener nuestro propio metodo'''

class MiLista(list):
    def insertar_comienzo(self, item):
        self.insert(0, item)

l2 = MiLista(range(1,4,1))
l2.insertar_comienzo(0)
l2.append(4)
print(l2)