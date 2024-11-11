import pandas as pd  
from artistas import Artista  

class Biblioteca:  
    def __init__(self):  
        #Usar un DataFrame para almacenar artistas y sus canciones  
        self.__artistas_df = pd.DataFrame(['artista', 'cancion'])  
    
    def agregar_artista(self, nombre_artista, **kwargs):  
        #Crear el artista solo si no existe   
        if nombre_artista not in self.__artistas_df['artista'].values:  
            artista = Artista(nombre_artista, **kwargs)  
            for cancion in artista.canciones_populares:  
                nueva_fila = pd.DataFrame({'artista': [artista.nombre], 'cancion': [cancion.titulo]})  
                self.__artistas_df = pd.concat([self.__artistas_df, nueva_fila])  

    def obtener_artistas(self):  
        return self.__artistas_df['artista'].unique()  #Retorna una lista de artistas unicos  

    def obtener_cancion(self, titulo_cancion, nombre_artista):  
        #Buscar una cancion específica dentro del DataFrame  
        if nombre_artista in self.__artistas_df['artista'].values:  
            canciones_encontradas = self.__artistas_df[  
                (self.__artistas_df['artista'] == nombre_artista),  
                (self.__artistas_df['cancion'].str.lower() == titulo_cancion.lower())  
            ]  
            if not canciones_encontradas.empty:  
                return canciones_encontradas  
        return None  

    def listar_artistas(self):  
        #Listar todos los artistas y sus canciones  
        for nombre_artista in self.obtener_artistas():  
            print(f"Artista: {nombre_artista}")  
            canciones = self.__artistas_df[self.__artistas_df['artista'] == nombre_artista]['cancion']  
            for cancion in canciones:  
                print(f"  - {cancion}")