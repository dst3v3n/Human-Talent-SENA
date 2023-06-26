from Usuario import *
from Ubicacion import *
from Oferta import *
from Postular import *

class Empresa (Usuario):
    def __init__(self, Id: int, Nombre: str,Nit:int, Telefono: int, Correo: str, Password: str):
        Usuario.__init__(self, Id, Nombre, Telefono, Correo, Password)
        self.__nit = Nit
        self.__name_depar = None
        self.__name_municipio = None
        

    def agregar_ubicacion (self , Name_Depar:str , Name_Municipio:str):
        self.__name_depar = Name_Depar
        self.__name_municipio = Name_Municipio


    def Agregar_postulacion (self, habilidades:list , jornada_laboral:list , requerimientos_especiales:list):
        obj1 = Postulacion (habilidades , jornada_laboral , requerimientos_especiales)

    
    def setNit (self,Nit:int):
        self.__nit = Nit

    def getNit (self):
        return self.__nit