from datos import Datos  

class Cancion(Datos):  
    def __init__(self, titulo, artista, **kwargs):  
        super().__init__(titulo, **kwargs)  
        self.__artista = artista  
        for llave, valor in kwargs.items():  
            setattr(self, llave, valor)  

    @property  
    def artista(self):  
        return self.__artista  

    @property  
    def titulo(self):  
        return self.nombre  

    def __str__(self):  
        return f"{self.titulo} de {self.artista}"