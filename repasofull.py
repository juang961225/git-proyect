#notas estudiante, promedio por estudiante, datos estudiante
# (carne, nombre, carrera, semestre), notas y porcentaje de cd nota
# numero de estudiantes acumulados y promedio de todos los 
#estudiantes acumulados y decir si gano o perdio, si saca mayor a 2.5 y menor a 3.0 puede recuperar

estudiante = True
numeroEstudiantes = 0
promedioEstudiantes = 0

while estudiante:    
    nombre = input('Digite su nombre: ')
    carne = input('Digite el numero de su carne: ')
    carrera = input('Digite el nombre de su carrera: ')
    semestre =  input('Digite el numero del semestre en que va: ')
    porcentaje = 0
    promedio = 0

    try:
        valCarne = int(carne)
        valSemestre = int(semestre)

        while porcentaje <= 99:
            nota = float(input('Porfavor Digite la nota: '))
            porcentNota = float(input('Digite el numero del porcentaje de esa nota: '))
            porcentaje = porcentaje + porcentNota
            promedio = promedio + (nota*(porcentNota/100))
            print('El porcentaje acumulado de las notas es de: ', porcentaje, '%')
            print('El porcentaje que falta por ingresar es de: ', (100 - porcentaje), '%', 'Porfavor siga ingresando...')
            
        print('Señor/a', nombre, ' cuyo carne es: ', carne, ' Tiene una nota final de: ', promedio)

        numeroEstudiantes = numeroEstudiantes + 1
        promedioEstudiantes = promedioEstudiantes + promedio

        if promedio >= 3.0:
            print('Mi perro, Ganaste')
        elif promedio >= 2.5:
            print('Mi perro, a recuperar')
        else:
            print('Llorelo mi papa')
    except ValueError:
        print("porfavor digite numeros en: Semestre, carne, Nota, porcentaje")
    
    print('El total de estudiantes es de: ', numeroEstudiantes)
    print('Y la nota general de todos es de: ', (promedioEstudiantes/numeroEstudiantes))

    respuesta = input('Hay mas estudiantes? responda Y/N: ')
    if respuesta == 'Y':
        estudiante = True
    elif respuesta == 'y':
        estudiante = True
    else:
        estudiante = False

print('Final Final... no va mas.')