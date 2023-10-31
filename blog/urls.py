# blog/urls.py
from django.urls import path
from .views import write_blog, view_blogs

urlpatterns = [
    path('write/', write_blog, name='write'),
    path('view/', view_blogs, name='list'),
    # other patterns...
]
