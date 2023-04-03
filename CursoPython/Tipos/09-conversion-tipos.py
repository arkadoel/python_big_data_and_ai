x = input(">")


"""
int()
str() transforma a string
float() transforma a real
bool() dependiendo del tipo de dato lo transforma:
    Truthy              Falsy
    -------             --------
    True                False
    "False"             ""
                        0 cero
                        None
"""
print(bool(""))
print(bool("0"))
print(bool(None))
print(bool(" "))
print(bool(0))
