from cancion import Cancion  

class Artista:  
    def __init__(self, nombre, **kwargs):  
        self.nombre = nombre  
        self.canciones_populares = self.cargar_canciones(**kwargs)  
  
        for llave, valor in kwargs.items():  
            setattr(self, llave, valor)  

    def cargar_canciones(self, **kwargs):  
        canciones_por_artista = {  
            "Feid": ["Feliz Cumpleaños", "Porfa", "Luna"],  
            "Ed Sheeran": ["Shape of You", "Perfect", "Bad Habits"],  
            "Queen": ["We are the champions", "Bohemian Rhapsody", "Love of my life"]  
        }  

        canciones = []  
        if self.nombre in canciones_por_artista:  
            for titulo in canciones_por_artista[self.nombre]:  
                canciones.append(Cancion(titulo, self.nombre, **kwargs))  
        
        return canciones

    def __str__(self):  
        return self.nombre