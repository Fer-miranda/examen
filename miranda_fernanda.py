import csv
import random
import statistics

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
lista_trabajadores = []

def asignar_sueldos():
    for trabajador in trabajadores:
        nombre = trabajador
        sueldo = random.randint(300000, 2500000)
        lista_trabajadores.append({
            'nombre': nombre,
            'sueldo': sueldo
        })
    print("Sueldos asignados exitosamente")

def listar():
    for trabajador in lista_trabajadores:
        print(f"NOMBRE: {trabajador['nombre']}\nSUELDO: {trabajador['sueldo']}\n")

def clasificar_sueldos():
    menores = []
    medianos = []
    altos = []
    for trabajador in lista_trabajadores:
        if trabajador['sueldo'] < 800000:
            menores.append(trabajador)
        elif trabajador['sueldo'] >= 800000 and trabajador['sueldo'] < 2000000:
            medianos.append(trabajador)
        elif trabajador['sueldo'] >= 2000000:
            altos.append(trabajador)
    
    print(f"Sueldos menores a $800.000 TOTAL: {len(menores)}")
    for trabajador in menores:
        print(f"NOMBRE: {trabajador['nombre']}\nSUELDO: {trabajador['sueldo']}")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(medianos)}")
    for trabajador in medianos:
        print(f"NOMBRE: {trabajador['nombre']}\nSUELDO: {trabajador['sueldo']}")
    print(f"Sueldos superiores a $2.000.000 TOTAL: {len(altos)}")
    for trabajador in altos:
        print(f"NOMBRE: {trabajador['nombre']}\nSUELDO: {trabajador['sueldo']}")
    
    sueldos = []
    for trabajador in lista_trabajadores:
        sueldos.append(trabajador['sueldo'])
    print(f"TOTAL SUELDOS: {sum(sueldos)}")

def estadisticas():
    sueldos = []
    for trabajador in lista_trabajadores:
        sueldos.append(trabajador['sueldo'])
    maximo = max(sueldos)
    minimo = min(sueldos)
    promedio = sum(sueldos)/len(sueldos)
    media_geo = statistics.geometric_mean(sueldos)
    print(f"ESTADÍSTICAS\nSueldo máximo: {maximo}\nSueldo mínimo: {minimo}\nPromedio: {promedio}\nMedia Geométrica: {media_geo}")


def reporte_sueldos():
    for trabajador in lista_trabajadores:
        sueldos = trabajador['sueldo']
        descuento_afp = sueldos*0.12
        descuento_salud = sueldos*0.07
        sueldo_liquido = sueldos - (descuento_afp + descuento_salud)
        trabajador['afp'] = descuento_afp
        trabajador['salud'] = descuento_salud
        trabajador['sueldo liquido'] = sueldo_liquido
    generar_archivo(lista_trabajadores, 'lista_de_trabajadores.csv')

def generar_archivo(lista_trabajadores, archivo):
    with open(archivo, 'w', newline="") as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=lista_trabajadores[0])
        writer.writeheader()
        for trabajador in lista_trabajadores:
            writer.writerow(trabajador)
        print("Archivo generado exitosamente")

def salir():
    print(f"Finalizando programa...\nDesarrollado por Fernanda Miranda\nRUT: 18.613.621-7")
    exit()

def menu():
    while True:
        option = int(input(f"Selecciona una opción:\n 1. Asignar Sueldos\n 2. Clasificar Sueldos\n 3. Ver estadísticas\n 4. Reporte de sueldos\n 5. Salir\nOPCIÓN: "))
        if option == 1:
            asignar_sueldos()
        elif option == 2:
            clasificar_sueldos()
        elif option == 3:
            estadisticas()
        elif option == 4:
            reporte_sueldos()
        elif option == 5:
            salir()
        elif option == 6:
            listar()
menu()