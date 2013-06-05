__author__ = 'tfaris'

import time

from celery.task import Task
from celery.registry import tasks


class DummyTaskOne(Task):
    def run(self, sleep=20):
        print "DummyTaskOne sleeping for %s seconds" % sleep
        time.sleep(sleep)
        print "DummyTaskOne wakes up!"

tasks.register(DummyTaskOne)