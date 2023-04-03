"""
python al igual que C/C++ evalua las sentencias if de izquierda a derecha
en el caso de que el primer parametro de un and ya sea falso, no va a seguir 
evaluando el resto de operaciones. Ejemplo:

if not gas and encendido and edad >17:

si gas no es True, ya no sigue evaluando el resto de elementos.

con el or pasa al reves, si la primera variable es True ya no sigue con las 
siguientes porque ya debe entrar

"""
