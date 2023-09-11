class Filtro:

    def __init__(self):
        self.__rango_salario = None
        self.__rango_exp = None
        self.__tipo_ocupacion = None
        self.__ubicacion_des = None
        self.__horario_des = None
        self.__tipo_contr_des = None
        self.__teletrabajo = None

    #setters#

    def setRango_salario (self,Rango_salario:str):
        self.__rango_salario = Rango_salario

    def setRango__exp (self, Rango__exp:str):
        self.__rango_exp = Rango__exp
    
    def setTipo_ocupacion (self,Tipo_ocupacion:str):
        self.__tipo_ocupacion = Tipo_ocupacion

    def setUbicacion_des (self,Ubicacion_des:str):
        self.__ubicacion_des = Ubicacion_des

    def setHorario_des (self,Horario_des:str):
        self.__horario_des = Horario_des

    def setTipo_contr_des (self,Tipo_contr_des:str):
        self.__tipo_contr_des = Tipo_contr_des
    
    def setTeletrabajo (self,Teletrabajo: bool):
        self.__teletrabajo = Teletrabajo 

    #getters#

    def getRango_salario (self):
        return self.__rango_salario
    
    def getRango_exp (self):
        return self.__rango_exp
    
    def getTipo_ocupacion (self):
        return self.__tipo_ocupacion
    
    def getUbicacion_des (self):
        return self.__ubicacion_des
    
    def getHorario_des (self):
        return self.__horario_des
    
    def getTipo_contr_des (self):
        return self.__tipo_contr_des
    
    def getTeletrabajo (self):
        return self.__teletrabajo
