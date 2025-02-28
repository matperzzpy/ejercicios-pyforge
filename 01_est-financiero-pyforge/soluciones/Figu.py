nombre = input("ingrese su nombre :")
edad =input("ingrese su edad  :")
clase_baja = 781120
clase_media = 4206033 
clase_alta = 4206033
ingreso_trabajo =int(input("inserte su ingreso por trabajo "))
Ingreso_inversiones = int(input("inserte su ingreso por inversiones "))
ingreso_activos =int(input("inserte su ingreso por activos "))

gastos_impuestos=int(input("inserte sus gastos por impuestos "))
gastos_lujos = int(input("inserte sus gastos por lujos "))
gastos_deudas = int(input("inserte sus gastos por deudas "))
otros_gastos = int(input("inserte otros gastos "))

ingresos_totales  = ingreso_trabajo + Ingreso_inversiones + ingreso_activos 

gastos_totales = gastos_impuestos + gastos_lujos + gastos_deudas + otros_gastos

ingreso_neto = ingresos_totales - gastos_totales

if ingreso_neto >= clase_alta :
    print("perteneces a la clase alta ")
elif ingreso_neto >= clase_media :
    print("perteneces a la clase media ")
else : 
    print("perteneces a la clase baja ")
