from celery import shared_task
import time

@shared_task
def ejemplo_lento():
    time.sleep(5)
    print("Tarea completada")
    return "Finalizado"