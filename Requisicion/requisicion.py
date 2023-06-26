from sys import path 
path.append("C:\Human-Talent-SENA\Postulacion")
from seleccion.Empresa import *
from seleccion.Oferta import *
from seleccion.Ubicacion import *
from seleccion.Usuario import *
from seleccion.Educacion import *
from seleccion.Cargo import *

class requisicion:
    def __init__(self,id_requisicion,manual_funciones, horario_laboral,
                 tipo_salario,fecha_solicitud,salario,tipo_ponderacion):
        self.__id_requisicion = id_requisicion
        self.__manual_funciones = manual_funciones
        self.__fecha_solicitud = fecha_solicitud
        self.__tipo_ponderacion = tipo_ponderacion
        self.__tipo_salario = tipo_salario
        self.__horario_laboral = horario_laboral
        self.__salario=salario
        self.__requisitos_edu = None
        self.__cupos_vacantes = None
        self.__dependencia = None 

        ### Agregar empresa ###
def Empresa (self,Id, nit:int, name_departamento:None,name_municipio:None):
    obj1 = Empresa (Id,nit ,name_departamento, name_municipio)
    ### Agregar educacion ##
def Educacion (self,Tipo:str , Name_Institucion:str , Titulacion:str , Fecha_fin:str ):
    obj1 = Educacion (Tipo,Name_Institucion,Titulacion,Fecha_fin )


        ### setters ###
def setmanual_funciones (self,name:str,manual_funciones:str):
     for i in self.__manual_funciones:
        if name == i:
            indice = self.__manual_funciones.index(i)
            self.__tipo.pop(indice)
            self.__tipo.insert(indice)

def setfecha_solicitud (self,fecha_solicitud:str):
    self.__fecha_solicitud = fecha_solicitud
def settipo_ponderacion (self,name:str,tipo_ponderacion:str):
    for i in self.__tipo_ponderacion:
        if name == i:
            indice = self.__tipo_ponderacion.index(i)
            self.__tipo.pop(indice)
            self.__tipo.insert(indice)

def settipo_salario (self,tipo_salario:str):
    self.__tipo_salario =tipo_salario
def setsalario (self,salario:str,antiguo:str, nuevo:str):
    for i in self.__salario:
        if antiguo == i:
            indice = self.__salario.index(i)
            self.__salario.pop(indice)
            self.__salario.insert(indice, nuevo )

def sethorario_laboral (self,horario_laboral):
    self.__horario_laboral= horario_laboral
def setrequisitos_edu (self,requisitos):
    self.__requisitos = requisitos
def setcupos_vacantes (self,cupos_vacantes):
    self.__cupos_vacantes= cupos_vacantes
def setdependencia(self,dependencia):
    self.__dependencia= dependencia

### getters ###
def getmanual_funciones(self):
    return self.__manual_funciones
def gettipo_ponderacion (self):
    return self.__tipo_ponderacion 
def gethorario_laboral(self):
    return self.__horario_laboral
def gettipo_salario(self):
    return self.__horario_laboral







