from sys import path 
path.append("C:\Human-Talent-SENA")
from requisicion import *
from Postulacion.Empresa import *
from Postulacion.Oferta import *
from Postulacion.Ubicacion import *
from Postulacion.Usuario import *
from Postulacion.Educacion import *
from Postulacion.Cargo import *

obj1 = requisicion (1, "manual funciones", 12/12/2012,"actual", "bachicherato",4,"laboral")
obj2 = Empresa (4, "Acarreos txt" ,1543, 332343322 , "acareos.sena.com" , "acareos expres")
obj6 = Oferta (1028 , 10 , "10/20/2015" , "15/21/2016","2000000", "6 meses", "Indefinido")
obj4= Ubicacion ("tolma","la mesa")
obj5= Usuario (12,"camila",32132132,"zully3323@gmail","deas")
obj3 = Educacion ()
obj7 = Cargo (1021 , 10 , "mesero" , "excelente")


print("obj1.gettipo_ponderacion")
print("obj1.gethorario_laboral")