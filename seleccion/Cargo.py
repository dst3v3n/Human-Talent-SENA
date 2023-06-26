from sys import path

path.append("..\\Human-Talent-SENA")

from Seleccion.Oferta import *

class Cargo:
    def __init__(self,Codigo_Cno:int, Nombre:str, Descripcion:str , Competencia:list):
        self.__codigo_cno = Codigo_Cno
        self.__nombre_cargo = Nombre
        self.__descripcion = Descripcion
        self.__competencia = Competencia
        self.__codigo = None
        self.__num_vacante = None
        self.__fecha_inicio = None
        self.__fecha_cierre = None
        self.__rango_salarial = None
        self.__experiencia = None
        self.__tipo_contrato = None
        self.__teletrabajo = None


    ### Agregar Oferta ###
    
    def agregar_oferta (self, codigo_oferta:int ,  num_vacante:int, fecha_inicio:str , fecha_cierre:str , rango_salaria:list , experiencia:str , tipo_contrato:str , teletrabajo: bool = False):
        self.__codigo = codigo_oferta
        self.__num_vacante = num_vacante
        self.__fecha_inicio = fecha_inicio
        self.__fecha_cierre = fecha_cierre
        self.__rango_salarial = rango_salaria
        self.__experiencia = experiencia
        self.__tipo_contrato = tipo_contrato
        self.__teletrabajo = teletrabajo

    ### Setters ###

    def setCno (self, Codigo_Cno:int):
        self.__codigo_cno = Codigo_Cno
    
    def setNombre (self, Nombre:str):
        self.__nombre_cargo = Nombre
    
    def setDescripcion (self , Descripcion:str):
        self.__descripcion = Descripcion
    
    def setCompetencia (self, Name:str , Actualizacion:str):
        for i in self.__competencia:
            if Name == i:
                indice = self.__competencia.index(i)
                self.__competencia.pop(indice)
                self.__competencia.insert(indice , Actualizacion)
    
    ### Getters ###

    @property
    def getCno (self):
        return self.__codigo_cno
    
    @property
    def getNombre (self):
        return self.__nombre_cargo
    
    @property
    def getDescripcion (self):
        return self.__descripcion
    
    @property
    def getCompetencia (self):
        return self.__competencia