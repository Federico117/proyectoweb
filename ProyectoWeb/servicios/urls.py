from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from servicios import views


urlpatterns = [
    path('', views.servicios, name="Servicios"),
]
