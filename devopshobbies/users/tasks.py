from celery import shared_task
from .services import profile_count_update
@shared_task
def hello2():
    print("hello")

@shared_task
def profile_update():
    profile_count_update()