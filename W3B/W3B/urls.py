"""
Definition of urls for W3B.
"""

from django.conf.urls import *
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.w3b)
]


