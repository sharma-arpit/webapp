from celery import Celery
import config


def make_celery():
    celery_queue = Celery(__name__, broker=config.CELERY_BROKER)
    celery_queue.conf.update(config.as_dict())
    return celery_queue


celery = make_celery()
