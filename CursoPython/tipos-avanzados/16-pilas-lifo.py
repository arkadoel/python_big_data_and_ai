pila = []

pila.append(1)
pila.append(2)
pila.append(3)
print(pila)
ultimpo_elemento = pila.pop()
print(pila)
pila.pop()
pila.pop()

if not pila:
    print("pila vacia")