
print('Programa para Calcular cuanto se ordeño de leche por animal\n')

# Variables utilizadas como contadores y acumuladores
volumen_meta_minima = 10
minimo_volumen = 0.5
maximo_volumen = 1.5

total_vacas = 0
total_cabras = 0
total_bufalas = 0

volumen_vacas = 0
volumen_cabras = 0
volumen_bufalas = 0

# Variables requeridas en el ciclo de control
volumen_recolectado = 0

# Mientras el volumen recolectado sea menor a la meta mínima
while volumen_recolectado <= volumen_meta_minima:
    volumen_ordeñado = float(input(f'Ingrese el volumen de ordeño obtenido: '))

    #Si el volumen no está en el rango válido, se continua en el ciclo sin modificar el volumen recolectado
    if volumen_ordeñado < minimo_volumen or volumen_ordeñado > maximo_volumen:
        print('Volumen inválido. Intenta nuevamente\n')
        continue

    tipo_animal = input('Ingrese el tipo de animal: ').lower()

    #Si el tipo de animal no es de los esperados, se continua en el ciclo sin modificar el volumen recolectado
    if tipo_animal != 'vaca' and tipo_animal != 'cabra' and tipo_animal != 'búfala':
        print('Tipo de animal inválido. Intenta nuevamente\n')
        continue

    if tipo_animal == 'vaca':
        total_vacas += 1
        volumen_vacas += volumen_ordeñado

    if tipo_animal == 'cabra':
        total_cabras += 1
        volumen_cabras += volumen_ordeñado

    if tipo_animal == 'búfala':
        total_bufalas += 1
        volumen_bufalas += volumen_ordeñado

    #Sentencia de salida: recalcular el volumen recolectado para saber si se cumplió la meta
    volumen_recolectado = volumen_cabras + volumen_vacas + volumen_bufalas

    if volumen_recolectado <= volumen_meta_minima:
        print(f'El volumen recolectado hasta el momento es {volumen_recolectado:.2f} lts, falta mínimo {(volumen_meta_minima - volumen_recolectado):.2f} lts\n')
    else:
        print('Meta alcanzada!')

# Visualizacion de resultados
print('\n*** Resultados Obtenidos *** \n')
print(f'Cabras: Total cabras ordeñadas: {total_cabras}, total volumen obtenido {volumen_cabras:.2f} lts.')
print(f'Búfalas: Total búfalas ordeñadas: {total_bufalas}, total volumen obtenido {volumen_bufalas:.2f} lts.')
print(f'Vacas: Total vacas ordeñadas: {total_vacas}, total volumen obtenido {volumen_vacas:.2f} lts.')

print(f'\nEn total se obtuvo una producción de {volumen_recolectado:.2f} Lts')
