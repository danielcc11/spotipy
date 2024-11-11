#Imports estandar
import os  
import time 

#Imports locales 
from usuario import Usuario  
from biblioteca import Biblioteca  
from playlist import Playlist  
from reproductor import Reproductor  
from excepciones import UsuarioError, CancionError, NombreUsuarioInvalido, ContraseñaInvalida  

#Funcion para limpiar la pantalla  
def limpiar_pantalla():  
    os.system('clear')  

class Menu:  
    def __init__(self):  
        self.biblioteca = Biblioteca()  
        self.usuarios = []  
        self.usuario_actual = None  
        self.reproductor = Reproductor()  
        self.cargar_artistas()  

    def cargar_artistas(self):  
        artistas = ["Feid", "Ed Sheeran", "Queen"]  
        for artista in artistas:  
            self.biblioteca.agregar_artista(artista)  

    def validar_nombre_usuario(self, nombre_usuario):  
        if not nombre_usuario:  
            raise NombreUsuarioInvalido("El nombre de usuario no puede estar vacio.")  
        if len(nombre_usuario) < 3:  
            raise NombreUsuarioInvalido("El nombre de usuario debe tener al menos 3 caracteres.")   

    def validar_contraseña(self, contraseña):  
        if len(contraseña) < 8:  
            raise ContraseñaInvalida("La contraseña debe tener al menos 8 caracteres.")  

    def registrar_usuario(self):  
        while True:  
            try:#Validar nombre de usuario  
                nombre_usuario = input("Ingrese su nombre de usuario: ")  
                self.validar_nombre_usuario(nombre_usuario)   
                contraseña = input("Ingrese su contraseña: ")  
                self.validar_contraseña(contraseña) 
                self.usuario_actual = Usuario(nombre_usuario, contraseña)  
                self.usuarios.append(self.usuario_actual)  
                print("Usuario registrado exitosamente.")  
                break  
            except (NombreUsuarioInvalido) as e:  
                print(f"Error: {e}. Intente de nuevo.")
            except (ContraseñaInvalida) as e:
                print(f"Error: {e}. Intente de nuevo.")  

    def reproducir_cancion(self, playlist):  
        try:  
            seleccion = int(input("Seleccione el numero de la cancion que desea reproducir: "))  

            if seleccion > 0 and seleccion <= len(playlist.canciones):  
                cancion_reproducida = playlist.canciones[seleccion - 1]  
                self.reproductor.reproducir(cancion_reproducida)  
            else:  
                raise CancionError("Numero de selección fuera de rango.")  
        except ValueError:  
            raise CancionError("Entrada inválida. Debe ingresar un numero.")  

    def mostrar_menu(self):  
        print("Bienvenido a SPOTIPY.\n\nPor favor inicia sesion.")  
        self.registrar_usuario()  

        while True:  
            limpiar_pantalla()  
            print("\nOpciones:")  
            print("1. Mostrar biblioteca")  
            print("2. Crear playlist aleatoria")  
            print("3. Crear playlist manual")  
            print("4. Cerrar sesion")  

            opcion = input("Seleccione una opcion: ")  

            try:  
                if opcion == '1':  
                    limpiar_pantalla()  
                    print(f"\nBiblioteca de artistas y canciones:")  
                    self.biblioteca.listar_artistas()  
                    time.sleep(8)  
                elif opcion == '2':  
                    limpiar_pantalla()  
                    nombre_playlist = input("Ingrese el nombre de la lista de reproduccion: ") 
                    mi_playlist = Playlist(nombre_playlist, self.biblioteca)  
                    mi_playlist.crear_playlist_aleatoria()  
                    mi_playlist.reproducir()  

                    reproducir = input("¿Deseas reproducir alguna cancion de la lista de reproduccion? (s/n): ").lower()  
                    if reproducir == 's':  
                        self.reproducir_cancion(mi_playlist)  
                    time.sleep(3)  
                elif opcion == '3':  
                    limpiar_pantalla()  
                    nombre_playlist = input("Ingrese el nombre de la lista de reproduccion: ")  
                    mi_playlist = Playlist(nombre_playlist, self.biblioteca)  
                    mi_playlist.crear_playlist_manual()  
                    mi_playlist.reproducir()  

                    reproducir = input("¿Deseas reproducir alguna cancion de la lista de reproduccion? (s/n): ").lower()  
                    if reproducir == 's':  
                        self.reproducir_cancion(mi_playlist)  
                    time.sleep(3)  
                elif opcion == '4':  
                    limpiar_pantalla()  
                    print("Cerraste sesion. ¡Hasta luego!")  
                    break  
                else:  
                    raise UsuarioError("Opcion no válida. Por favor, intente de nuevo.")  
            except UsuarioError as ue:  
                limpiar_pantalla()  
                print(f"Error de usuario: {ue}")  
                time.sleep(2)  
            except CancionError as ce:  
                limpiar_pantalla()  
                print(f"Error de cancion: {ce}")  
                time.sleep(2)  
            except Exception as e:  
                limpiar_pantalla()  
                print(f"Ocurrió un error inesperado: {e}")  
                time.sleep(2)