from sys import path

path.append("..\\Human-Talent-SENA")
from seleccion.Oferta import *
from Filtro import *
class Resultados:
    
    def __init__ (self):
        self.__codigo_oferta = None
        self.__num_vacante = None
        self.__fecha_inicio = None
        self.__fecha_cierre = None
        self.__rango_salaria = None
        self.__experiencia = None
        self.__tipo_contrato = None
        self.__teletrabajo = None
        self.__rango_salario = None
        self.__rango_exp = None
        self.__tipo_ocupacion = None
        self.__ubicacion = None
        self.__horario_des = None
        self.__tipo_conta_des = None

    # Agregar oferta #

    def agregar_oferta (self , Codigo_oferta:int ,  Num_vacante:int, Fecha_inicio:str , Fecha_cierre:str , Rango_salaria:list , Experiencia:str , Tipo_contrato:str , Teletrabajo: bool = False):
        self.__codigo_oferta = Codigo_oferta
        self.__num_vacante = Num_vacante
        self.__fecha_inicio = Fecha_inicio
        self.__fecha_cierre = Fecha_cierre
        self.__rango_salaria = Rango_salaria
        self.__experiencia = Experiencia
        self.__tipo_contrato = Tipo_contrato
        self.__teletrabajo = Teletrabajo
    
    # Agregar filtro#

    def agregar_filtro (self, Name:str, Rango_salario:str= False, Rango_exp:str= False, Tipo_ocupacion:str= False, Ubicacion_des:str=False, Horario_des:str=False, Tipo_contr_des:str= False, Teletrabajo:bool = False ):
        if Rango_salario == True:
            self.__rango_salario = Name

        elif Rango_exp == True:
            self.__rango_exp = Name

        elif Tipo_ocupacion == True:
            self.__tipo_ocupacion = Name

        elif Ubicacion == True:
            self.__ubicacion = Name

        elif Horario_des == True:
            self.__horario_des = Name    
        elif Tipo_contr_des == True:
            self.__tipo_conta_des = Name

        
        else:
            self.__teletrabajo = Name



    #setters

    def setresultado(self, Resultado:int):
        self.__resultado = Resultado

    def setfiltro(self, Filtro:int):
        self.__filtro = Filtro


    #getters

    def getresultado (self):
        return self.__resultado
    
    def getfiltro (self):
        return self.__filtro 