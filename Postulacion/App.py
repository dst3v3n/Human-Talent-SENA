from Usuario import *
from Aspirante import *
from Empresa import *
from Educacion import *


obj1 = Aspirante (1 , "Harold" , "Sabogal" , 3143442062 , "haroldsaboga48@gmail.com" , "Harold")
obj2 = Empresa (2 , "Human Talent Sena" ,1024, 3143442062 , "HumanTalent@gmail.com" , "Human talent")
obj3 = Educacion ()

obj1.agregar_educacion ("Basica" , "Depar" , "Basica Primaria", "10/20/2015")

print(obj1.getFecha_fin)
print(obj1.getTitulacion)
print(obj1.getName_institucion)

obj1.setFecha_fin("10/20/2015" , "10/75/2017")
obj1.setTitulacion("Basica Primaria" , "Baschillerato Academico")
obj1.setName_institucion ("Depar" , "Institucion Educativa Compartir")
obj1.setTipo ("Basica" , "Bachillerato")

print(obj1.getFecha_fin)
print(obj1.getTitulacion)
print(obj1.getName_institucion)
print(obj1.getTipo)