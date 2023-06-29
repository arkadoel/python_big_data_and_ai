#se trata de ver como un objeto puede contener otros objetos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self) -> str:
        return f"Producto: {self.nombre} - Precio: {self.precio}"

class Categoria:
    productos = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

kayak = Producto("kayak", 1000)
bicicleta = Producto("bicicleta", 750)
surfboard= Producto("surftboard", 500)
deportes = Categoria("deportes", [kayak, bicicleta])
deportes.agregar(surfboard)
deportes.imprimir()