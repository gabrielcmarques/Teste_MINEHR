from django.urls import path
from . import views 


urlpatterns = [
    path('', views.plot_dados, name="plot_dados"),
]