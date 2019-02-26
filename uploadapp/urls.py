# from django.contrib import admin
from django.urls import path

from .views import upload_canvas

urlpatterns = [
    path('', upload_canvas),
]
