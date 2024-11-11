class Usuario:  
    def __init__(self, nombre_usuario, contraseña, **kwargs):  
        self.__nombre_usuario = nombre_usuario  
        self.__contraseña = contraseña  
        self.__biblioteca = []  
        
        for llave, valor in kwargs.items():  
            setattr(self, llave, valor)  

    def agregar_cancion(self, cancion):  
        self.__biblioteca.append(cancion)  

    def obtener_biblioteca(self):  
        return self.__biblioteca  

    def agregar_usuario(self, usuario):  
        self.__usuario.append(usuario)  

    def obtener_usuarios(self):  
        return self.__usuario  

    @property  
    def nombre_usuario(self):  
        return self.__nombre_usuario  

    @property  
    def contraseña(self):  
        return self.__contraseña