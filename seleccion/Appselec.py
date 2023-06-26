from Usuario import *
from Aspirante import *
from Empresa import *
from Educacion import *
from Oferta import *
from Postular import *

aspirante1 = Aspirante (1 , "Laura" , "Rosero" , 3118465214 , "laurosero@gmail.com" , "12345")
empresa1 = Empresa (2 , "Human Talent Sena" ,1024, 3143442062 , "HumanTalent@gmail.com" , "Human talent")
edu1 = Educacion ()
salario = ["$1100000" , "2000000"]

#informacion postulacion
habilidades=["comunicacion", "liderazgo"]
jornada_laboral= ["noche 10 a 7 am", "mañana de 6am a 2 pm"]
requerimientos_especiales=["manejo de ingles", "manejo de plataformas"]
oferta1 = Oferta (1028 , 2 , "24/06/2023" , "30/06/2023" , salario , "12 meses" , "Contrato a termino Indefinido")
postularme1 = Postulacion (habilidades, jornada_laboral , requerimientos_especiales)

aspirante1.agregar_educacion ("Pregrado" , "Universidad Uniminuto" , "Ingenieria sistemas", "04/12/2020")

print(aspirante1.getFecha_fin)
print(aspirante1.getTitulacion)
print(aspirante1.getName_institucion)

aspirante1.setFecha_fin("04/12/2020" , "05/12/2022")
aspirante1.setTitulacion("Ingenieria sistemas" , "Especializacion")
aspirante1.setName_institucion ("Universidad Uniminuto" , "UNAD")
aspirante1.setTipo ("Pregrado" , "Posgrado")

print(aspirante1.getFecha_fin)
print(aspirante1.getTitulacion)
print(aspirante1.getName_institucion)
print(aspirante1.getTipo)

print(postularme1.Postular(1, "Laura", "Rosero", 3144410022, "laurarosero@gmail.com", "Laura"))
print(postularme1.Postular(1, "Laura", "Rosero", 3144410022 , "laurarosero@gmail.com", "laura"))
postularme1.enlistar_postulantes()