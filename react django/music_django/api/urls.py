
from django.urls import path, include
from .views import Roomview
urlpatterns = [
    path('room',Roomview.as_view())
]