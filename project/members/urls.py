from django.urls import path
from . import views
from re_framework import routers
urlpatterns = [
    path('members/', views.members, name='members'),
]



# if settings.DEBUG:
    # urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)