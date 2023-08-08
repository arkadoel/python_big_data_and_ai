"""
Fer, esta es la documentacion de player
"""

class Player:
    """
    Esta clase crea un reproductor de musica
    """

    def play(self, song:str):
        """
        Reproduce la cancion que recivio
        
        Parameters:
        song (str): este es un string con el path de la cancion

        Returns:
        int: devuelve 1 si reproduce correctamente, sino devuelve cero
        """
        