class Cargo:
    def __init__(self,Codigo_Cno:int, Nombre:str, Descripcion:str , Competencia):
        self.__codigo_cno = Codigo_Cno
        self.__nombre_cargo = Nombre
        self.__descripcion = Descripcion
        self.__Competencia = [Competencia]