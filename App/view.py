"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import time
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("---------------------------------------")
    print("\n")
    print("Bienvenido")
    print("1- incializando catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Contar avistamientos en una city")
    print("4- Contar avistamientos por duración")
    print("5- Contar avistamientos por hora/minutos del día")
    print("6- Contar avistamientos en un rango de fechas")
    print("7- Contar avistamientos de una zona geográfica")
    print("\n")
    print("---------------------------------------")
def printReq1(map,city):
    cant = om.size(map)
    print("Hay " + str(cant) + " avistamientos en: " + str(city))
    print("Los primeros y ultimos 3 son: ")
    range = 3
    mapRec = map 
    a = 1
    while a <= range:
        key = om.minKey(mapRec)
        keyPair = om.get(mapRec,key)
        value = me.getValue(keyPair)
        print("-------------------------------")
        print("Date time: " + str(value["datetime"]))
        print("City: " + str(city))
        print("State: "+ str(value["state"]))
        print("Country: " + str(value["country"]))
        print("Shape: " + str(value["shape"]))
        print("Duration (seconds): " + str(value["duration (seconds)"]))
        mapRec = om.deleteMin(mapRec)
        a+=1
    x = 1 
    while x <= range and om.size(mapRec) >= 1:
        key = om.maxKey(mapRec)
        keyPair = om.get(mapRec,key)
        value = me.getValue(keyPair)
        print("-------------------------------")
        print("Date time: " + str(value["datetime"]))
        print("City: " + str(city))
        print("State: "+ str(value["state"]))
        print("Country: " + str(value["country"]))
        print("Shape: " + str(value["shape"]))
        print("Duration (seconds): " + str(value["duration (seconds)"]))
        mapRec = om.deleteMax(mapRec)
        x +=1 
def printReq5(map):
    print("There are " + str(om.size(map)) + " different UFO sightings in the current area")
    print("The first 5 and last 5 UFO sightings in this time are: ")
    mapRec = map
    if om.size(map) >= 10:
        rango = 5
        i = 1
        while i <= rango:
            llave = om.minKey(mapRec)
            keyPair = om.get(mapRec,llave)
            element = me.getValue(keyPair)
            value = lt.getElement(element,0)
            print("-------------------------------")
            print("Date time: " + str(value["datetime"]))
            print("City: " + str(value["city"]))
            print("State: "+ str(value["state"]))
            print("Country: " + str(value["country"]))
            print("Shape: " + str(value["shape"]))
            print("Duration (seconds): " + str(value["duration (seconds)"]))
            print("latitude: " + str(value["latitude"]))
            print("longitude: " + str(value["longitude"]))
            mapRec = om.deleteMin(mapRec)
            i+=1
        j = 1 
        while j <= rango and om.size(mapRec) >= 1:
            llave = om.maxKey(mapRec)
            keyPair = om.get(mapRec,llave)
            element = me.getValue(keyPair)
            value = lt.getElement(element,0)
            print("-------------------------------")
            print("Date time: " + str(value["datetime"]))
            print("City: " + str(value["city"]))
            print("State: "+ str(value["state"]))
            print("Country: " + str(value["country"]))
            print("Shape: " + str(value["shape"]))
            print("Duration (seconds): " + str(value["duration (seconds)"]))
            print("latitude: " + str(value["latitude"]))
            print("longitude: " + str(value["longitude"]))
            mapRec = om.deleteMax(mapRec)
            j +=1 
    else:
        rango = om.size(map)
        i = 1
        while i <= rango:
            llave = om.minKey(mapRec)
            keyPair = om.get(mapRec,llave)
            element = me.getValue(keyPair)
            value = lt.getElement(element,0)
            print("-------------------------------")
            print("Date time: " + str(value["datetime"]))
            print("City: " + str(value["city"]))
            print("State: "+ str(value["state"]))
            print("Country: " + str(value["country"]))
            print("Shape: " + str(value["shape"]))
            print("Duration (seconds): " + str(value["duration (seconds)"]))
            print("latitude: " + str(value["latitude"]))
            print("longitude: " + str(value["longitude"]))

            mapRec = om.deleteMin(mapRec)
            i+=1




catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
    elif int(inputs[0]) == 2:
        print("Cargando información de los avistamientos... ")
        start_time = time.process_time()
        controller.loadData(catalog,"UFOS/UFOS-utf8-large.csv")
        print("Se han cargado los datos exitosamente")
        print("Total de datos cargados: " + str(lt.size(catalog["avistamiento"])))
        stop_time = time.process_time()
        elapsed_time_mseg = round((stop_time - start_time)*1000, 2)
        print("Tiempo:", elapsed_time_mseg, "mseg")
    elif int(inputs[0]) == 3:
        city = input("Ingrese la city que desea consultar: ")
        mapCity = controller.AvistamientosPorcity(catalog,city)
        print('Altura del arbol: ' + str(controller.indiceAltura(mapCity)))
        print('elements en el arbol: ' + str(controller.indiceTamaño(mapCity)))
        printReq1(mapCity,city)
        
    elif int(inputs[0]) == 4:
        print("Hay " + str(om.size(catalog["Duracion"])) + " duraciones de avistamientos ")
        print("El avistamiento más largo es: ")
        max = om.maxKey(catalog["Duracion"])
        pareja = om.get(catalog["Duracion"], max)
        valor = me.getValue(pareja)
        tamaño = lt.size(valor)
        print("Date: " + str(max) + "count: " + str(tamaño))
        fecha1 = input("Ingrese la primera duracion: ")
        fecha2 = input("Ingrese la segunda duracion: ")
        llaves = controller.avistamientosbyDuration(catalog,fecha1,fecha2)




    elif int(inputs[0]) == 5:
        print("avistamientos con la hora y minuto del día (formato HH:MM) más tardíos que se tengan registrados: "+ str(om.valueSet(catalog["Fechas"])))
        print("El avistamiento más antiguo es: ")
        viejo = om.minKey(catalog["Fechas"])
        keyPair = om.get(catalog["Fechas"], viejo)
        value = me.getValue(keyPair)
        size = lt.size(value)
        print("Date: " + str(viejo) + "count: " + str(size))

    
    elif int(inputs[0]) == 6:
        print("Hay " + str(om.size(catalog["Fechas"])) + " avistamientos de UFO en diferentes fechas [YYYY-MM-DD]")
        print("El avistamiento más antiguo es: ")
        viejo = om.minKey(catalog["Fechas"])
        keyPair = om.get(catalog["Fechas"], viejo)
        value = me.getValue(keyPair)
        size = lt.size(value)
        print("Date: " + str(viejo) + "count: " + str(size))
        fecha1 = input("Ingrese la primera fecha en formato (YYYY-MM-DD): ")
        date1 = time.strptime(fecha1, '%Y-%m-%d')
        fecha2 = input("Ingrese la segunda fecha en formato (YYYY-MM-DD): ")
        date2 = time.strptime(fecha2, '%Y-%m-%d')
        keys = controller.fechasEnRango(catalog,date1,date2)
    elif int(inputs[0]) == 7:
        longInf = float(input("Ingrese el limite inferior de longitud: "))
        longMay = float(input("Ingrese el limite superior de longitud: "))
        latInf = float(input("Ingrese el limite inferior de latitud: "))
        latMay = float(input("Ingrese el limite superior de latitud: "))
        map = controller.AvistamientosEnRango(catalog,longInf,longMay,latInf,latMay)
        printReq5(map)
    else:
        sys.exit(0)
sys.exit(0)