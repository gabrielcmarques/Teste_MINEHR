from django.contrib import admin
from django.urls import path, include

from plot_dados import urls

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('plot_dados.urls')),
    path('api/', include('api.urls')),
]
