import pandas as pd  

class Usuario:  
    def __init__(self, nombre_usuario, contraseña, **kwargs):  
        self.__nombre_usuario = nombre_usuario  
        self.__contraseña = contraseña  
        self.__biblioteca = pd.DataFrame(['cancion'])  #Inicializa un DataFrame vacio para la biblioteca  
        self.__usuarios = pd.DataFrame(['nombre_usuario', 'contraseña'])  #DataFrame para manejar otros usuarios  
        
        for llave, valor in kwargs.items():  
            setattr(self, llave, valor)  

    def agregar_cancion(self, cancion):  
        nueva_fila = pd.DataFrame({'cancion': [cancion]})  
        self.__biblioteca = pd.concat([self.__biblioteca, nueva_fila])  #Agrega la cancion al DataFrame  

    def obtener_biblioteca(self):  
        return self.__biblioteca['cancion'].tolist()  #Retorna la lista de canciones  

    def agregar_usuario(self, nombre_usuario, contraseña):  
        nueva_fila = pd.DataFrame({'nombre_usuario': [nombre_usuario], 'contraseña': [contraseña]})  
        self.__usuarios = pd.concat([self.__usuarios, nueva_fila])  #Agrega el nuevo usuario al DataFrame  

    def obtener_usuarios(self):  
        return self.__usuarios[['nombre_usuario', 'contraseña']]  #Retorna el DataFrame de usuarios  

    @property  
    def nombre_usuario(self):  
        return self.__nombre_usuario  

    @property  
    def contraseña(self):  
        return self.__contraseña