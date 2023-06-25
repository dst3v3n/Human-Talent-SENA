from Ubicacion import *
from Aspirante import *

class Oferta:
    def __init__(self , codigo_oferta:int ,  num_vacante:int, fecha_inicio:str , fecha_cierre:str , rango_salaria:list , experiencia:str , tipo_contrato:str , teletrabajo: bool = False):
        self.__codigo = codigo_oferta
        self.__num_vacante = num_vacante
        self.__fecha_inicio = fecha_inicio
        self.__fecha_cierre = fecha_cierre
        self.__rango_salarial = rango_salaria
        self.__experiencia = experiencia
        self.__tipo_contrato = tipo_contrato
        self.__teletrabajo = teletrabajo
        self.__name_depar = None
        self.__name_municipio = None
        self.__codigo_cno = None
        self.__nombre_cargo = None
        self.__descripcion = None
        self.__competencia = []


    ### Agregar Ubicacion ###

    def agregar_ubicacion (self , Name_Depar:str , Name_Municipio:str):
        self.__name_depar = Name_Depar
        self.__name_municipio = Name_Municipio

    ### Agregar Aspirante ###
    
    def Aspirante (self,Id, Nombre, Apellido , Telefono, Correo, Password):
        obj1 = Aspirante (Id , Nombre , Apellido , Telefono , Correo , Password)

    ### Setters ###

    def setCodigo (self, Codigo:int):
        self.__codigo = Codigo
    
    def setNum_vacantes (self, Num_Vacante: int):
        self.__num_vacante = Num_Vacante
    
    def setFecha_inicio (self , Fecha_Inicio: str):
        self.__fecha_inicio = Fecha_Inicio

    def setFecha_cierre (self , Fecha_Cierre: str):
        self.__fecha_cierre = Fecha_Cierre
    
    def setRango_salarial (self, Anterior :str , Nuevo:str):
        for i in self.__rango_salarial:
            if Anterior == i:
                indice = self.__rango_salarial.index(i)
                self.__rango_salarial.pop(indice)
                self.__rango_salarial.insert(indice , Nuevo)
    
    def setExperiencia (self, Experiencia:str):
        self.__experiencia = Experiencia
    
    def setTipo_contrato (self, Tipo_Contato:str):
        self.__tipo_contrato = Tipo_Contato
    
    def setTeletrabajo (self, Teletrabajo: bool = False):
        self.__teletrabajo = Teletrabajo

    
    ### Getters

    @property 
    def getCodigo (self):
        return self.__codigo

    @property 
    def getNum_vacante (self):
        return self.__num_vacante
    
    @property 
    def getFecha_inicio (self):
        return self.__fecha_inicio
    
    @property 
    def getFecha_cierre (self):
        return self.__fecha_cierre
    
    @property 
    def getRango_Salarial (self):
        return self.__rango_salarial
    
    @property 
    def getExperiencia (self):
        return self.__experiencia
    
    @property 
    def getTipo_contrato (self):
        return self.__tipo_contrato
    
    @property 
    def getTeletrabajo (self):
        return self.__teletrabajo