from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import rbmq.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'RabbitMQTest.views.home', name='home'),
    # url(r'^RabbitMQTest/', include('RabbitMQTest.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^task$', rbmq.views.running_tasks),
    url(r'^task/(\d+)$', rbmq.views.dummy_task_starter)
)
