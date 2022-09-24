from django.urls import path

from . import views

urlpatterns=[
    path("", views.index, name="index"), # it will render index from views.index if you leave the path empty meaning http://127.0.0.1:8000/flights/
    path("<int:flight_id>", views.flight, name="flight")
]