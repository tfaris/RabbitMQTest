from urlparse import urlparse

from django.conf import settings

import celery
from celery.task.control import inspect

import pika
__author__ = 'tfaris'

GET_COUNT_CHANNEL = 31234


def get_queued_count():
    count = 0
    p = get_connection()
    channel = None
    try:
        channel = p.channel(GET_COUNT_CHANNEL)
        queue = channel.queue_declare(queue='celery', passive=True)
        count = queue.method.message_count
    finally:
        if channel:
            channel.close()
        p.close()
    return count


def get_active_count():
    count = 0
    insp = inspect()
    count += _get_task_count(insp.active())
    count += _get_task_count(insp.scheduled())
    return count


def _get_task_count(inspect_info):
    count = 0
    # Looks like the following:
    # {u'name': [{u'args': u'[]', u'time_start': 1370404676.74, u'name': u'rbmq.tasks.DummyTaskOne', u'delivery_info': {u'priority': None, u'routing_key': u'celery', u'exchange': u'celery'}, u'hostname': u'beast3', u'acknowledged': True, u'kwargs': u'{}', u'id': u'09c96f3f-c847-476d-8587-a9264155911b', u'worker_pid': 8316}]}
    if inspect_info:
        for host_name, tasks in inspect_info.iteritems():
            count += len(tasks)
    return count


def get_incomplete_count():
    return get_queued_count() + get_active_count()


def get_connection():
    url = urlparse(settings.BROKER_URL)
    creds = pika.PlainCredentials(url.username, url.password)
    return pika.BlockingConnection(pika.ConnectionParameters(host=url.hostname,
                                                             virtual_host=url.path[1:],
                                                             credentials=creds))
