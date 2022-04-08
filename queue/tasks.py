import os
import pandas as pd
from celery import Celery


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.count')
def count() -> str:
    df = pd.read_json('tweets_short.json', lines=True)
    tweets = df[~df['coordinates'].isnull()]
    return f"{len(tweets)} tweets"
