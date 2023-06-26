class Usuario:
    def __init__ (self, Id:int, Nombre:str, Telefono:int , Correo:str , Password:str):
        self.__id = Id
        self.__nombre = Nombre
        self.__telefono = Telefono
        self.__correo = Correo
        self.__password = Password

    def setId (self,Id:int):
        self.__id= Id

    def setNombre (self, Nombre:str):
        self.__nombre = Nombre
    
    def setTelefono (self, Telefono:int):
        self.__telefono = Telefono
    
    def setCorreo (self, Correo:str):
        self.__correo = Correo
    
    def setPassword (self, Password:str):
        self.__password = Password


    def getId (self):
        return self.__id
    
    
    def getNombre (self):
        return self.__nombre
    
    
    def getTelefono (self):
        return self.__telefono
    
    
    def getCorreo (self):
        return self.__correo
    
    def getPassword (self):
        return self.__password