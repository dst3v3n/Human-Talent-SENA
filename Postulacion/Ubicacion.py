class Ubicacion:
    def __init__(self , Name_Depar:str , Name_Municipio:str):
        self.__name_depar = Name_Depar
        self.__name_municipio = Name_Municipio
        self.__codigo_depar = None
        self.__codigo_municipio = None

    
    ### Setters ###

    def setName_depar (self, Name_Depar:str):
        self.__name_depar = Name_Depar

    def setName_municipio (self, Name_Municipio:str):
        self.__name_municipio = Name_Municipio
    
    def setCodigo_depar (self , Codigo_Depar:int):
        self.__codigo_depar = Codigo_Depar

    def setCodigo_municipio (self , Codigo_Municipio:int):
        self.__codigo_municipio = Codigo_Municipio

    
    ### Getters ###

    @property
    def getName_depar (self):
        return self.__name_depar
    
    @property
    def getName_municipio (self):
        return self.__name_municipio
    
    @property
    def getCodigo_depar (self):
        return self.__codigo_depar
    
    @property
    def getCodigo_municipio (self):
        return self.__codigo_municipio