class Usuario:
    def __init__ (self, Id:int, Nombre:str, Telefono:int , Correo:str , Password:str):
        self.__id = Id
        self.__nombre = Nombre
        self.__telefono = Telefono
        self.__correo = Correo
        self.__password = Password

    ### Setters ###

    def setNombre (self, Nombre:str):
        self.__nombre = Nombre
    
    def setTelefono (self, Telefono:int):
        self.__telefono = Telefono
    
    def setCorreo (self, Correo:str):
        self.__correo = Correo
    
    def setPassword (self, Password:str):
        self.__password = Password

    ### Getters ###

    @property
    def getId (self):
        return self.__id
    
    @property
    def getNombre (self):
        return self.__nombre
    
    @property
    def getTelefono (self):
        return self.__telefono
    
    @property
    def getCorreo (self):
        return self.__correo
    
    @property
    def getPassword (self):
        return self.__password