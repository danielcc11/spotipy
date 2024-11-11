import random  
from cancion import Cancion  

class Playlist:  
    def __init__(self, nombre, biblioteca):  
        self.nombre = nombre  
        self.biblioteca = biblioteca  
        self.canciones = []  

    def crear_playlist_aleatoria(self):  
        todas_las_canciones = []  
        for artista in self.biblioteca.obtener_artistas().values():  
            todas_las_canciones.extend(artista.canciones_populares)  
        
        self.canciones = random.sample(todas_las_canciones, min(len(todas_las_canciones), 6))  
        print(f"Playlist aleatoria '{self.nombre}' creada con {len(self.canciones)} canciones.")  

    def crear_playlist_manual(self):  
        print("Creando playlist...")  
        while True:  
            titulo = input("Introduce el titulo de la cancion (o 'fin' para terminar): ")  
            if titulo.lower() == 'fin':  
                break  
            
            artista = input("Introduce el nombre del artista: ")  
            cancion = self.biblioteca.obtener_cancion(titulo, artista)  
            
            if cancion:  
                self.canciones.append(cancion)  
                print(f"'{cancion.titulo}' ha sido añadida a la playlist.")  
            else:  
                print(f"No se encontro la cancion '{titulo}' de '{artista}' en la biblioteca.")  
    
    def reproducir(self):  
        print(f"Lista de canciones en la playlist '{self.nombre}':")  
        for i, cancion in enumerate(self.canciones, 1):  
            print(f"{i}. {cancion.titulo} - {cancion.artista}")