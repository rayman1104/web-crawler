"""
    Celery tasks. Some of them will be launched periodically from admin panel via django-celery-beat
"""
from typing import List

from app.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task()
def crawl(url: str) -> List[str]:
    return [url, 'qwe', 'asd']
