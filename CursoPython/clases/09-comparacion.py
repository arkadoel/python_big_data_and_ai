class Coordenadas:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro) -> bool:
        return self.lat == otro.lat and self.lon == otro.lon
    '''en cuanto implementamos __eq__ python hace por inferencia el
        __ne__ que es lo contrario
        lo mismo pasara con el metodo __lt__ que hara que se genere 
        automaticamente el metodo __le__ (less or equal)

    '''
    
    
coords = Coordenadas(47, 27)
coords2 = Coordenadas(47, 27)

print(coords == coords2) 
''' dara False porque para comparar objetos se hace
    de la siguiente manera. Debemos usar __eq__ y
    entonces la comparacion anterior dara True
'''