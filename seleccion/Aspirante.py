from sys import path

path.append("..\\Human-Talent-SENA")

from Seleccion.Usuario import *
from Seleccion.Educacion import *
from Seleccion.Experiencia import *

class Aspirante (Usuario):
    def __init__(self, Id: int, Nombre: str, Apellido: str, Telefono: int, Correo: str, Password: str):
        Usuario.__init__(self,Id, Nombre, Telefono, Correo, Password)
        self.__apellido = Apellido
        self.__tipo = []
        self.__name_institucion = []
        self.__titulacion = []
        self.__fecha_fin = []
        self.__fecha_inicio_ex = []
        self.__fecha_fin_ex = []
        self.__name_empresa = []
        self.__funciones = []
        self.__cargo = []

    ### Añadir Educacion ###

    def agregar_educacion (self, Tipo:str , Name_Institucion:str , Titulacion:str , Fecha_fin:str):
        self.__tipo.append (Tipo)
        self.__name_institucion.append (Name_Institucion)
        self.__titulacion.append (Titulacion)
        self.__fecha_fin.append (Fecha_fin)

    ### Añadir Experiencia ###

    def agregar_experiencia (self, Fecha_Inicio:str , Fecha_Fin:str , Name_Empresa:str , Funciones:str , Cargo:str):
        self.__fecha_inicio_ex.append (Fecha_Inicio)
        self.__fecha_fin_ex.append (Fecha_Fin)
        self.__name_empresa.append (Name_Empresa)
        self.__funciones.append (Funciones)
        self.__cargo.append(Cargo)

    ### Setters ###

    def setApellido (self , Apellido:str):
        self.__apellido = Apellido

    def setName_institucion (self , Name:str , Actualizacion:str):
        for i in self.__name_institucion:
            if Name == i:
                indice = self.__name_institucion.index(i)
                self.__name_institucion.pop(indice)
                self.__name_institucion.insert(indice , Actualizacion)
    
    def setTitulacion (self , Name:str , Actualizacion:str):
        for i in self.__titulacion:
            if Name == i:
                indice = self.__titulacion.index(i)
                self.__titulacion.pop(indice)
                self.__titulacion.insert(indice , Actualizacion)
    
    def setFecha_fin (self , Name:str , Actualizacion:str):
        for i in self.__fecha_fin:
            if Name == i:
                indice = self.__fecha_fin.index(i)
                self.__fecha_fin.pop(indice)
                self.__fecha_fin.insert(indice , Actualizacion)

    def setTipo (self , Name:str , Actualizacion:str):
        for i in self.__tipo:
            if Name == i:
                indice = self.__tipo.index(i)
                self.__tipo.pop(indice)
                self.__tipo.insert(indice , Actualizacion)

    ### Getters ###

    @property
    def getApellido (self):
        return self.__apellido
    
    @property
    def getTipo (self):
        return self.__tipo
    
    @property
    def getName_institucion (self):
        return self.__name_institucion

    @property
    def getTitulacion (self):
        return self.__titulacion

    @property
    def getFecha_fin (self):
        return self.__fecha_fin