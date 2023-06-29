class MiError(Exception):
    "esta clase es para representar mi error"
    def __init__(self, mensaje,codigo_error) -> None:
        self.mensaje = mensaje
        self.codigo = codigo_error

    def __str__(self) -> str:
        return f"{self.mensaje} - codigo {self.codigo}"


def division(n=0):
    if n == 0:
        raise MiError("no puedes dividor por cero", 400)
    return 5/n

try:
    division()
except MiError as ex:    
    print(ex)