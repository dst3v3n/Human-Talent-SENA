from sys import path

path.append("..\\Human-Talent-SENA")

from Seleccion.Aspirante import *
from Seleccion.Empresa import *
from Seleccion.Experiencia import *
from Seleccion.Oferta import *
from Seleccion.Cargo import *
from Seleccion.Postular import *
from Seleccion.Ubicacion import *
from Seleccion.Educacion import *


###Postulacion###
salario = ["$1100000" , "2000000"]
competencia = ["Porgramar" , "Analista"]
obj1 = Aspirante (1 , "Harold" , "Sabogal" , 3143442062 , "haroldsaboga48@gmail.com" , "Harold")
obj2 = Empresa (2 , "Human Talent Sena" ,1024, 3143442062 , "HumanTalent@gmail.com" , "Human talent")
obj3 = Cargo (1028,"Ingenieria Sistemas" , "Ingenieria Sistemas" , competencia)
obj4 = Oferta (1028 , 10 , "10/20/2015" , "15/21/2016" , salario , "6 meses" , "Indefinido")
obj5 = Postulacion (salario , salario , salario)

print("¿Que modulo quieres saber?")
print("1. Postulacion")
print("2. Si te quieres salir de la app")
modulo = int(input("Digita el modulo que quieres gestionar: "))
match modulo:
    case 1:
        print("Que clase quieres gestionar?")
        print("1. Aspirante") 
        print("2. Empresa") 
        print("3. Oferta") 
        print("4. Cargo") 
        print("5. Postulacion") 
        clases = 1
        while clases != 0 :
            clases = int(input("Digita la clase que quieres gestionar: "))
            match clases:
                case 1:
                    print("Que quieres hacer con esta clase?")
                    print("1. Getters")
                    print("2. Setters")
                    opciones = int(input("Digita la opcion que quieres hacer: "))
                    match opciones:
                        case 1:
                            print(obj1.getNombre)
                            print(obj1.getApellido)
                            print(obj1.getTelefono)
                            print(obj1.getCorreo)
                            print(obj1.getPassword)
                        case 2:
                            print("¿Que quieres editar?")
                            print("1. Nombre")
                            print("2. Apellido")
                            print("3. Telefono")
                            print("4. Correo")
                            print("5. Password")
                            sete = int(input("Digita lo que quieres modificar: "))
                            match sete:
                                case 1:
                                    x = input("Digita la modificacion: ")
                                    obj1.setNombre(x)
                                case 2:
                                    x = input("Digita la modificacion: ")
                                    obj1.setApellido (x)
                                case 3:
                                    x = input("Digita la modificacion: ")
                                    obj1.setTelefono (x)
                                case 4:
                                    x = input("Digita la modificacion: ")
                                    obj1.setCorreo (x)
                                case 5:
                                    x = input("Digita la modificacion: ")
                                    obj1.setPassword (x)
                case 2:
                    print("Que quieres hacer con esta clase?")
                    print("1. Getters")
                    print("2. Setters")
                    opciones = int(input("Digita la opcion que quieres hacer: "))
                    match opciones:
                        case 1:
                            print(obj2.getNombre)
                            print(obj2.getNit)
                            print(obj2.getTelefono)
                            print(obj2.getCorreo)
                            print(obj2.getPassword)
                        case 2:
                            print("¿Que quieres editar?")
                            print("1. Nombre")
                            print("2. Nit")
                            print("3. Telefono")
                            print("4. Correo")
                            print("5. Password")
                            sete = int(input("Digita lo que quieres modificar: "))
                            match sete:
                                case 1:
                                    x = input("Digita la modificacion: ")
                                    obj2.setNombre(x)
                                case 2:
                                    x = input("Digita la modificacion: ")
                                    obj2.setNit (x)
                                case 3:
                                    x = input("Digita la modificacion: ")
                                    obj2.setTelefono (x)
                                case 4:
                                    x = input("Digita la modificacion: ")
                                    obj2.setCorreo (x)
                                case 5:
                                    x = input("Digita la modificacion: ")
                                    obj2.setPassword (x)
                case 3:
                    print("Que quieres hacer con esta clase?")
                    print("1. Getters")
                    print("2. Setters")
                    opciones = int(input("Digita la opcion que quieres hacer: "))
                    match opciones:
                        case 1:
                            print(obj4.getCodigo)
                            print(obj4.getNum_vacante)
                            print(obj4.getFecha_inicio)
                            print(obj4.getFecha_cierre)
                            print(obj4.getRango_Salarial)
                            print(obj4.getExperiencia)
                            print(obj4.getTipo_contrato)
                            print(obj4.getTeletrabajo)
                        case 2:
                            print("¿Que quieres editar?")
                            print("1. Codigo")
                            print("2. Numero de vacantes")
                            print("3. Fehcha de inicio")
                            print("4. Fecha de cierre")
                            print("5. Rango Salarial")
                            print("6. Experiencia")
                            print("7. Tipo de contrato")
                            print("8. Teletrabajo")
                            sete = int(input("Digita lo que quieres modificar: "))
                            match sete:
                                case 1:
                                    x = int(input("Digita la modificacion: "))
                                    obj4.setCodigo(x)
                                case 2:
                                    x = int(input("Digita la modificacion: "))
                                    obj4.setNum_vacantes (x)
                                case 3:
                                    x = input("Digita la modificacion: ")
                                    obj4.setFecha_inicio (x)
                                case 4:
                                    x = input("Digita la modificacion: ")
                                    obj4.setFecha_cierre (x)
                                case 5:
                                    y = input ("Que quieres editar: ")
                                    x = input("Digita la modificacion: ")
                                    obj4.setRango_salarial (y , x)
                                case 6:
                                    x = input("Digita la modificacion: ")
                                    obj4.setExperiencia (x)
                                case 7:
                                    x = input("Digita la modificacion: ")
                                    obj4.setTipo_contrato (x)
                                case 8:
                                    x = input("Digita la modificacion: ")
                                    obj4.setTeletrabajo (x)
                case 4:
                    print("Que quieres hacer con esta clase?")
                    print("1. Getters")
                    print("2. Setters")
                    opciones = int(input("Digita la opcion que quieres hacer: "))
                    match opciones:
                        case 1:
                            print(obj3.getCno)
                            print(obj3.getNombre)
                            print(obj3.getDescripcion)
                            print(obj3.getCompetencia)
                        case 2:
                            print("¿Que quieres editar?")
                            print("1. CodigoCno")
                            print("2. Nombre del cargo")
                            print("3. Descripcion")
                            print("4. Competencia")
                            sete = int(input("Digita lo que quieres modificar: "))
                            match sete:
                                case 1:
                                    x = input("Digita la modificacion: ")
                                    obj3.setCno(x)
                                case 2:
                                    x = input("Digita la modificacion: ")
                                    obj3.setNombre (x)
                                case 3:
                                    x = input("Digita la modificacion: ")
                                    obj3.setDescripcion (x)
                                case 4:
                                    y = input ("Que quieres editar: ")
                                    x = input("Digita la modificacion: ")
                                    obj3.setCompetencia (y , x)

                case 5:
                    print("Que quieres hacer con esta clase?")
                    print("1. Getters")
                    print("2. Setters")
                    opciones = int(input("Digita la opcion que quieres hacer: "))
                    match opciones:
                        case 1:
                            print(obj5.getEstado)
                            print(obj5.getHabilidades)
                            print(obj5.getJornada_laboral)
                            print(obj5.getRequerimientos)
                        case 2:
                            print("¿Que quieres editar?")
                            print("1. Estado")
                            print("2. Habilidades")
                            print("3. Jornada Laboral")
                            print("4. Requerimientos especiales")
                            sete = int(input("Digita lo que quieres modificar: "))
                            match sete:
                                case 1:
                                    x = input("Digita la modificacion: ")
                                    obj5.setEstado(x)
                                case 2:
                                    x = input("Digita la modificacion: ")
                                    obj5.setHabilidades (x)
                                case 3:
                                    x = input("Digita la modificacion: ")
                                    obj5.setJornada_laboral (x)
                                case 4:
                                    x = input("Digita la modificacion: ")
                                    obj5.setRequerimientos_especiales (x)
    case 2:
        pass