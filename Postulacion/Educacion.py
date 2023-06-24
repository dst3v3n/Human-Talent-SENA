class Educacion:
    def __init__(self):
        self.__tipo = []
        self.__name_institucion = []
        self.__titulacion = []
        self.__fecha_fin = []


    ### Agregar Educacion ###

    def agregar_educacion (self, Tipo:str , Name_Institucion:str , Titulacion:str , Fecha_fin:str):
        self.__tipo.append (Tipo)
        self.__name_institucion.append (Name_Institucion)
        self.__titulacion.append (Titulacion)
        self.__fecha_fin.append (Fecha_fin)

    ### Getters ###

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
    