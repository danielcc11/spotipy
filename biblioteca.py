from artistas import Artista  

class Biblioteca:  
    def __init__(self):  
        self.__artistas = {}  
    
    def agregar_artista(self, nombre_artista, **kwargs):  
        if nombre_artista not in self.__artistas:  
            self.__artistas[nombre_artista] = Artista(nombre_artista, **kwargs)  
            for llave, valor in kwargs.items():  
            	setattr(self, llave, valor)  

    def obtener_artistas(self):  
        return self.__artistas  

    def obtener_cancion(self, titulo, artista):  
        if artista in self.__artistas: 
            for cancion in self.__artistas[artista].canciones_populares:
                if cancion.titulo.lower() == titulo.lower(): 
                    return cancion  
        return None  

    def listar_artistas(self):  
        for artista in self.__artistas.values():  
            print(f"Artista: {artista.nombre}")  
            for cancion in artista.canciones_populares:  
                print(f"  - {cancion.titulo}") 