from sys import path

path.append("..\\Human-Talent-SENA")

from Postulacion.Usuario import *
from Postulacion.Ubicacion import *
from Postulacion.Oferta import *
from Postulacion.Postular import *

class Empresa (Usuario):
    def __init__(self, Id: int, Nombre: str,Nit:int, Telefono: int, Correo: str, Password: str):
        Usuario.__init__(self, Id, Nombre, Telefono, Correo, Password)
        self.__nit = Nit
        self.__name_depar = None
        self.__name_municipio = None
        
    ### Agregar Ubicacion ###

    def agregar_ubicacion (self , Name_Depar:str , Name_Municipio:str):
        self.__name_depar = Name_Depar
        self.__name_municipio = Name_Municipio

    ### Agregar Postulacion ###

    def Agregar_postulacion (self, habilidades:list , jornada_laboral:list , requerimientos_especiales:list):
        obj1 = Postulacion (habilidades , jornada_laboral , requerimientos_especiales)

    ### Crear Oferta ###

    def Crear_Oferta (self , codigo_oferta:int ,Nombre_cargo:str ,  num_vacante:int, fecha_inicio:str , fecha_cierre:str , rango_salaria:list , experiencia:str , tipo_contrato:str ,  Competencia:list , teletrabajo: bool = False):
        x = input("Digita el nombre del departamento: ")
        y = input("Digita el nombre del municipio: ")
        cno = input ("Digita el codigo cno: ")
        Descripcion = input ("Digita la descripcion: ")
        obj1 = Oferta (codigo_oferta , num_vacante , fecha_inicio , fecha_cierre , rango_salaria , experiencia , tipo_contrato , teletrabajo)
        obj1.agregar_ubicacion(x , y)
        obj1.agregar_cargo(cno , Nombre_cargo , Descripcion , Competencia)
        
    def enlistar_postulantes (self):
        for name in Aspirante.getNombre:
                print(name)
        for apellido in Aspirante.getApellido:
                print(apellido)


    @property
    def setNit (self,Nit:int):
        self.__nit = Nit
    
    @property
    def getNit (self):
        return self.__nit