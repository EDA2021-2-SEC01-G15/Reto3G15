"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import deleteElement, iterator, lastElement
from DISClib.DataStructures.bst import contains
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import orderedmap as om
import time
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {"avistamiento" : None,
                "city" : None}
    catalog["avistamiento"] = lt.newList(datastructure="ARRAY_LIST")
    catalog["city"] = mp.newMap(1000,maptype="CHAINING", loadfactor=0.5)
    catalog["Fechas"] = om.newMap(omaptype="RBT",comparefunction=cmpFecha)
    catalog["Longitud"] = om.newMap(omaptype="RBT",comparefunction=cmpFecha)
    return catalog

# Funciones para agregar informacion al catalog
def añadirAvistamiento (catalog,avistamiento):
    lt.addLast(catalog["avistamiento"],avistamiento)
    city = avistamiento["city"]
    duracion=avistamiento["duration (seconds)"]
    fechaSinHoraCompleta = avistamiento["datetime"]
    sinHora = fechaSinHoraCompleta.split()
    fechaSinHora = sinHora[0]
    date = time.strptime(fechaSinHora, '%Y-%m-%d')
    latCompleta = float(avistamiento["latitude"])
    longCompleta = float(avistamiento["longitude"])
    Latitud = round(latCompleta,2)
    Longitud = round(longCompleta,2)
    actualizarCiudad(catalog["city"],avistamiento,city)
    actualizarFechas(catalog["Fechas"],avistamiento,date)
    UpdateDuracion(catalog["Duracion"],avistamiento,duracion)
    ActualizarLong(catalog["Longitud"],avistamiento,Longitud,Latitud)
    return catalog
def actualizarCiudad(map,avistamiento,city):
    ciudadIn = mp.contains(map,city)
    if ciudadIn:
        keyPair = mp.get(map,city)
        value = me.getValue(keyPair)
        lt.addLast(value,avistamiento)
    else:
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        mp.put(map,city,lis)
def actualizarFechas (map,avistamiento,fechaSinHora):
    ciudadIn = om.contains(map,fechaSinHora)
    if ciudadIn:
        keyPair = om.get(map,fechaSinHora)
        value = me.getValue(keyPair)
        lt.addLast(value,avistamiento)
    else:
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        om.put(map,fechaSinHora,lis)
def ActualizarLong(map,avistamiento,longitud,latitud):
    ciudadIn = om.contains(map,float(longitud))
    if ciudadIn:
        keyPair = om.get(map,float(longitud))
        value = me.getValue(keyPair)
        latin = om.contains(value,float(latitud))
        if latin:
            latpair = om.get(value,float(latitud))
            latvalue = me.getValue(latpair)
            lt.addLast(latvalue,avistamiento)
        else:
            list2 = lt.newList(datastructure="ARRAY_LIST")
            lt.addLast(list2,avistamiento)
            om.put(value,float(latitud),list2)
    else:
        latmap = om.newMap(omaptype="RBT",comparefunction=cmpFecha)
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        om.put(latmap,float(latitud),lis)
        om.put(map,float(longitud),latmap)

        
def UpdateDuracion(map,avistamiento,duracion):
    existDur = mp.contains(map,duracion)
    if existDur:
        entry = mp.get(map,duracion)
        valor = me.getValue(entry)
        lt.addLast(valor,avistamiento)
    else:
        lis = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(lis,avistamiento)
        mp.put(map,duracion,lis)
# Funciones para creacion de datos

# Funciones de consulta
def AvistamientosPorcity(map,city):
    keyPair = mp.get(map,city)
    AvistamientosCity = om.newMap(omaptype="RBT",comparefunction=cmpFecha)
    if keyPair != None:
        AvistamientosPorcity = me.getValue(keyPair)
        a = 1
        while a <= lt.size(AvistamientosPorcity):
            avistamiento = lt.getElement(AvistamientosPorcity,a)
            fechaSinHora = avistamiento["datetime"]
            fechaSinHoraAcomparar = time.strptime(fechaSinHora, '%Y-%m-%d %H:%M:%S')
            om.put(AvistamientosCity,fechaSinHoraAcomparar,avistamiento)

            a += 1 
    return AvistamientosCity
def fechaSinHorasEnRango(map,fecha1,fecha2):
    keys = om.values(map,fecha1,fecha2)
    elements = lt.iterator(keys)
    i = 1 
    while i <= 3:
        elementos = next(elements)
        element = lt.getElement(elementos,0)
        print("-----------------------")
        print("Date time: " + str(element["datetime"]))
        print("City: " + str(element["city"]))
        print("State: "+ str(element["state"]))
        print("Country: " + str(element["country"]))
        print("Shape: " + str(element["shape"]))
        print("Duration (seconds): " + str(element["duration (seconds)"]))
        i +=1
    j = 1
    while j <= 3:
        elements = lt.removeLast(keys)
        element = lt.getElement(elements,0)
        print("-----------------------")
        print("Date time: " + str(element["datetime"]))
        print("City: " + str(element["city"]))
        print("State: "+ str(element["state"]))
        print("Country: " + str(element["country"]))
        print("Shape: " + str(element["shape"]))
        print("Duration (seconds): " + str(element["duration (seconds)"]))
        j += 1
def AvistamientosEnRango(map,longitudinf,longitudmay,latitudinf,latitudmay):
    avistamientos_m = om.newMap(omaptype="RBT",comparefunction=cmpFecha)
    longsenrango = om.values(map,longitudmay,longitudinf)
    iterator1 = lt.iterator(longsenrango)
    a = 1
    while a <= lt.size(longsenrango):
        element = next(iterator1)
        latsenrango = om.keys(element,latitudinf,latitudmay)
        iterator2 = lt.iterator(latsenrango)
        x = 1 
        while x <= lt.size(latsenrango):
            elemento2 = next(iterator2)
            keypair = om.get(element,elemento2)
            value = me.getValue(keypair)
            if lt.size(value) > 1:
                recLista(avistamientos_m, value)
            else: 
                latitud = float(lt.getElement(value,0)["latitude"])
                om.put(avistamientos_m,latitud,value) 
            x +=1
        a+=1
    return avistamientos_m

def avistamientosPorHoraMinutos(map,fecha1,fecha2):
    keys = om.values(map,fecha1,fecha2)
    elements = lt.iterator(keys)
    i = 1 
    while i <= 3:
        elementos = next(elements)
        element = lt.getElement(elementos,0)
        print("-----------------------")
        print("Date time: " + str(element["datetime"]))
        print("City: " + str(element["city"]))
        print("State: "+ str(element["state"]))
        print("Country: " + str(element["country"]))
        print("Shape: " + str(element["shape"]))
        print("Duration (seconds): " + str(element["duration (seconds)"]))
        i +=1
    j = 1
    while j <= 3:
        elements = lt.removeLast(keys)
        element = lt.getElement(elements,0)
        print("-----------------------")
        print("Date time: " + str(element["datetime"]))
        print("City: " + str(element["city"]))
        print("State: "+ str(element["state"]))
        print("Country: " + str(element["country"]))
        print("Shape: " + str(element["shape"]))
        print("Duration (seconds): " + str(element["duration (seconds)"]))
        j += 1

def avistamientosbyDuration(map,limmax,limmin):
    llaves = om.values(map,limmax,limmin)
    elements = lt.iterator(llaves)
    a=1
    while a<=3:
        elementos=next(elements)
        elemento = lt.getElement(elementos,0)
        print("-----------------------")
        print("Date time: " + str(elemento["datetime"]))
        print("City: " + str(elemento["city"]))
        print("State: "+ str(elemento["state"]))
        print("Country: " + str(elemento["country"]))
        print("Shape: " + str(elemento["shape"]))
        print("Duration (seconds): " + str(elemento["duration (seconds)"]))
        a +=1
    j = 1
    while j <= 3:
        elementos = lt.removeLast(llaves)
        elemento = lt.getElement(elementos,0)
        print("-----------------------")
        print("Date time: " + str(elemento["datetime"]))
        print("City: " + str(elemento["city"]))
        print("State: "+ str(elemento["state"]))
        print("Country: " + str(elemento["country"]))
        print("Shape: " + str(elemento["shape"]))
        print("Duration (seconds): " + str(elemento["duration (seconds)"]))
        j += 1


def recLista(avistamientos_m, value):
    iterator3 = lt.iterator(value)
    i = 1
    while i <= lt.size(value):
        if i > 1:
            elemento3 = next(iterator3)
            latitud = round(float(elemento3["latitude"]),3)
            om.put(avistamientos_m,latitud,value)
        else:
            element3 = next(iterator3)
            latitud = float(element3["latitude"])
            om.put(avistamientos_m,latitud,value)
        i+=1 
def indiceAltura(map):

    return om.height(map)


def indiceTamaño(map):

    return om.size(map)


# Funciones utilizadas para comparar elements dentro de una lista
def cmpFecha(date1,date2):
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1
def cmpTime(time1,time2):
    if time1==time2:
        return 0
    elif time1>time2:
        return 1
    else:
        return -1
def cmpLetras(duracion1,duracion2):
    if duracion1["country"]==duracion2["country"]:
        return 0
    elif duracion1["country"]>duracion2["country"]:
        return 1
    else:
        return -1
# Funciones de ordenamiento
