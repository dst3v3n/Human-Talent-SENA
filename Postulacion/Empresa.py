from Usuario import *

class Empresa (Usuario):
    def __init__(self, Id: int, Nombre: str,Nit:int, Telefono: int, Correo: str, Password: str):
        Usuario.__init__(self, Id, Nombre, Telefono, Correo, Password)
        self.__nit = Nit

    ### Setters ###

    def setNit (self,Nit:int):
        self.__nit = Nit
    
    ### Getters ###

    @property
    def getNit (self):
        return self.__nit