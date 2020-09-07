from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('empresas.urls')),
    path('', include('perfis_empresas.urls')),
    path('', include('perfis_usuarias.urls')),
    path('', include('usuarias.urls'))
]
