from collections import deque

pila = deque([1, 2])
pila.append(3)
pila.append(4)
pila.append(5)
pila.append(6)
print(pila)
pila.popleft()
print(pila)

if not pila:
    print("pila vacia")

