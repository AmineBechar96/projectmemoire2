
from django.urls import path
from .views import *


urlpatterns = [

    path('',home, name='home'),
    path('blogs/',blogs, name='blog'),
    path('blogs/<int:blog_id>',detaille, name='detaille'),
]
