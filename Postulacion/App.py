from Usuario import *
from Aspirante import *
from Empresa import *
from Educacion import *
from Oferta import *
from Postular import *


obj1 = Aspirante (1 , "Harold" , "Sabogal" , 3143442062 , "haroldsaboga48@gmail.com" , "Harold")
obj2 = Empresa (2 , "Human Talent Sena" ,1024, 3143442062 , "HumanTalent@gmail.com" , "Human talent")
obj3 = Educacion ()
salario = ["$1100000" , "2000000"]
obj4 = Oferta (1028 , 10 , "10/20/2015" , "15/21/2016" , salario , "6 meses" , "Indefinido")
obj5 = Postulacion (salario , salario , salario)

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

print(obj5.Postular(1 , "Harold" , "Sabogal" , 3143442062 , "haroldsaboga48@gmail.com" , "Harold"))
print(obj5.Postular(1 , "Harold" , "Sabogal" , 3143442062 , "haroldsaboga48@gmail.com" , "Harold"))
obj5.enlistar_postulantes()