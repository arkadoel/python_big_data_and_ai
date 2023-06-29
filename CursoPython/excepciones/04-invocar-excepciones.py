def division(n=0):
    if n == 0:
        raise ZeroDivisionError("no puedes dividor por cero")
    return 5/n

try:
    division()
except ZeroDivisionError as ex:
    print(ex)