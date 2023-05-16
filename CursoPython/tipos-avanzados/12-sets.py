#set significa grupo o grupo
#coleccion de datos que no se puede repetir y que tampoco esta ordenada
primer = {1,1,2,2,3,4}
print(primer) #elimina los duplicados cuando crea el set

primer.add(5)
primer.remove(1)
print(primer)

segundo = [3,4,5]
segundo = set(segundo)
print(segundo)

print(primer | segundo) #une los dos sets

print(primer & segundo) #interseccion pone los elementos que esten en ambos sets

print(primer - segundo) #diferencia, los datos que estan en primer excepto los elementos de segundo

print(primer ^ segundo) #direrencia simetrica, en el primero y en el segundo pero que no se encuentren duplicados

if 5 in segundo:
    print("esta")

#pero no podemos acceder mediante indice como primer[0]




