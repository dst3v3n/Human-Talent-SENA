class Experiencia :
    def __init__(self, Name_Empresa:str , Fecha_inicio:str , Fecha_Cierre, Cargo:str):
        self.__name_empresa = Name_Empresa
        self.__fecha_inicio = Fecha_inicio
        self.__fecha_cierre = Fecha_Cierre
        self.__cargo = Cargo
        self.__funciones = []

    
    def agregar_funciones (self, Funcion:str):
        self.__funciones.append(Funcion)


    def setName_empresa (self, Name_Empresa:str):
        self.__name_empresa = Name_Empresa

    def setFecha_inicio (self, Fecha_inicio:str):
        self.__fecha_inicio = Fecha_inicio

    def setFecha_cierre (self, Fecha_cierre:str):
        self.__fecha_cierre = Fecha_cierre
    
    def setCargo (self, Cargo:str):
        self.__cargo = Cargo
    
    def setFunciones (self, Name:str , Actualizacion:str):
        for i in self.__funciones:
              if Name == i:
                    indice = self.__funciones.index(i)
                    self.__funciones.pop(indice)
                    self.__funciones.insert(indice , Actualizacion)
    

    def getName_empresa (self):
        return self.__name_empresa
    
    def getFecha_inicio (self):
        return self.__fecha_inicio
    
    def getFecha_cierre (self):
        return self.__fecha_cierre
    
    def getCargo (self):
        return self.__cargo

    def getFunciones (self):
        return self.__funciones