from django.http import HttpResponse, Http404

from tasks import *
from amqp_util import get_incomplete_count


def dummy_task_starter(request, task_num):
    if task_num == "1":
        DummyTaskOne().delay()
    else:
        raise Http404
    return HttpResponse("Task Started (hopefully...)")


def running_tasks(request):
    count = get_incomplete_count()
    return HttpResponse("There are %s tasks either running or scheduled." % count)
