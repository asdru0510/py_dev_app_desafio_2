from desafioadl.models import Tarea, Subtarea
def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = Subtarea.objects.all()
    return tareas, subtareas
   

def crear_nueva_tarea(texto:str):
    tarea = Tarea(descripcion=texto)
    tarea.save()
    imprimir_en_pantalla()
    

def crear_sub_tarea(texto:str,tarea_id):
    tarea=Tarea.objects.get(id=tarea_id)
    subtarea = Subtarea(descripcion=texto,tarea_id=tarea)
    subtarea.save()
    imprimir_en_pantalla()

def elimina_tarea(id_tarea):
    tarea=Tarea.objects.get(id=id_tarea)
    tarea.eliminada=True
    tarea.save()
    imprimir_en_pantalla()

def elimina_sub_tarea(id_subtarea):
    subtarea=Subtarea.objects.get(id=id_subtarea)
    subtarea.eliminada=True
    subtarea.save()
    imprimir_en_pantalla()    


def imprimir_en_pantalla():
    tareas = Tarea.objects.all()
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion} - eliminada: {tarea.eliminada}")
        subtareas = Subtarea.objects.filter(tarea_id=tarea.id)  
        for subtarea in subtareas:
            print(f"    [{subtarea.id}] {subtarea.descripcion} - eliminada: {subtarea.eliminada}")

""" def imprimir_en_pantalla():
    tareas = Tarea.objects.all()
    for tarea_index, tarea in enumerate(tareas, start=1):
        print(f"[{tarea_index}] {tarea.descripcion} - Eliminada: {tarea.eliminada}")
        subtareas = Subtarea.objects.filter(tarea_id=tarea.id)
        for subtarea_index, subtarea in enumerate(subtareas, start=1):
            print(f"    [{subtarea_index}] {subtarea.descripcion} - Eliminada: {subtarea.eliminada}")
 """

    
""" 
from desafioadl.models import *
from desafioadl.services import * """