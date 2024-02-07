nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("Ingrese el salario del empleado: $ "))

horastrabajadas = int(input("Ingrese las horas trabajadas: "))
valorhora = salario / 47

# Calcular las horas extras
horassemanaleslaborales = 47
if horastrabajadas > horassemanaleslaborales:
    horasextras = horastrabajadas - horassemanaleslaborales
else:
    horasextras = 0

recargohorasextras = 0.35
valorhoraextra = valorhora * (1 + recargohorasextras)
pagobase = horastrabajadas * valorhora
totalhorasextras = horastrabajadas * valorhoraextra
salariototal = pagobase + (horasextras * pagobase / horassemanaleslaborales)

print("Las horas extras que trabajó ", nombre, "fueron: ", horasextras)
print("Valor hora extra : $ ", valorhoraextra)
print("Total horas extra: $ ", totalhorasextras)

print("El total de horas que trabajó ", nombre, "fueron : ", horastrabajadas)
print("El valor de la hora laboral ordinaria es : $ ", valorhora)
print("El valor Neto a pagar es : $ ", salariototal)




