from Aspirante import *

class Postulacion:
      counter = 0
      def __init__(self, habilidades:list , jornada_laboral:list , requerimientos_especiales:list):
            Postulacion.counter += 1
            self.__codigo_solicitud = None
            self.__estado = None
            self.__habilidades = habilidades
            self.__jornada_laborar = jornada_laboral
            self.__requerimientos_especiales = requerimientos_especiales
            self.__id = []
            self.__nombre = []
            self.__apellido = []
            self.__telefono = [] 
            self.__correo = []
            self.__password = None

            
      def Postular (self, Id: int, Nombre: str, Apellido: str, Telefono: int, Correo: str, Password: str):
            print ("Quiere realizar una postulacion para esta oferta")
            print ("1.Si")
            print ("2.No")
            selector = int(input())
            match selector:
                  case 1:
                        self.__estado = "Proceso de seleccion"
                        obj1 = Aspirante (Id , Nombre , Apellido , Telefono , Correo , Password)
                        self.__id.append(Id)
                        self.__nombre.append(Nombre)
                        self.__apellido.append(Apellido)
                        self.__telefono.append(Telefono)
                        self.__correo.append(Correo)  
                        self.__password = Password
                        return self.__estado
                  case 2:
                        print("No te postulaste")
            
      def enlistar_postulantes (self):
            for name in self.__nombre:
                  print(name)
            for apellido in self.__apellido:
                  print(apellido)

      def setEstado (self, Estado:str):
            self.__estado = Estado
      
      def setHabilidades (self, Name:str, Actualizacion:str):
            for i in self.__habilidades:
                  if Name == i:
                        indice = self.__habilidades.index(i)
                        self.__habilidades.pop(indice)
                        self.__habilidades.insert(indice , Actualizacion)

      def setJornada_laboral (self, Name:str, Actualizacion:str):
            for i in self.__jornada_laborar:
                  if Name == i:
                        indice = self.__jornada_laborar.index(i)
                        self.__jornada_laborar.pop(indice)
                        self.__jornada_laborar.insert(indice , Actualizacion)

      def setRequerimientos_especiales (self, Name:str, Actualizacion:str):
            for i in self.__requerimientos_especiales:
                  if Name == i:
                        indice = self.__requerimientos_especiales.index(i)
                        self.__requerimientos_especiales.pop(indice)
                        self.__requerimientos_especiales.insert(indice , Actualizacion)

      def getEstado (self):
            return self.__estado

      def getHabilidades (self):
            return self.__habilidades
      
      def getJornada_laboral (self):
            return self.__jornada_laborar

      def getRequerimientos (self):
            return self.__requerimientos_especiales