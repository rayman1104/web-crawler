"""
    Celery tasks. Some of them will be launched periodically from admin panel via django-celery-beat
"""

from app.celery import app
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@app.task(ignore_result=True)
def task() -> None:
    pass
