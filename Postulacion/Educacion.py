class Educacion:
    def __init__(self):
        self.__tipo = []
        self.__name_institucion = []
        self.__titulacion = []
        self.__fecha_fin = []


    def agregar_educacion (self, Tipo:str , Name_Institucion:str , Titulacion:str , Fecha_fin:str):
        self.__tipo.append (Tipo)
        self.__name_institucion.append (Name_Institucion)
        self.__titulacion.append (Titulacion)
        self.__fecha_fin.append (Fecha_fin)

    def setTipo (self, Name:str , Actualizacion:str):
        for i in self.__tipo:
            if Name == i:
                indice = self.__tipo.index(i)
                self.__tipo.pop(indice)
                self.__tipo.insert(indice , Actualizacion)

    def setName (self, Name:str , Actualizacion:str):
        for i in self.__name_institucion:
            if Name == i:
                indice = self.__name_institucion.index(i)
                self.__name_institucion.pop(indice)
                self.__name_institucion.insert(indice , Actualizacion)
    
    def setTitulacion (self, Name:str , Actualizacion:str):
        for i in self.__titulacion:
            if Name == i:
                indice = self.__titulacion.index(i)
                self.__titulacion.pop(indice)
                self.__titulacion.insert(indice , Actualizacion)
    
    def setFecha_fin  (self, fecha_anterior:str , Actualizacion:str):
        for i in self.__fecha_fin:
            if fecha_anterior == i:
                indice = self.__fecha_fin.index(i)
                self.__fecha_fin.pop(indice)
                self.__fecha_fin.insert(indice , Actualizacion)


    def getTipo (self):
        return self.__tipo


    def getName_institucion (self):
        return self.__name_institucion
    
    def getTitulacion (self):
        return self.__titulacion
    
    def getFecha_fin (self):
        return self.__fecha_fin