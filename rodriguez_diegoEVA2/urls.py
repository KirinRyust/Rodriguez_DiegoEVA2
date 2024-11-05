"""
URL configuration for rodriguez_diegoEVA2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from rodriguez_diegoEVA2APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('listarI/', views.listarInscripciones),
    path('agregarI/', views.agregarInscripciones),
    path('eliminarI/<int:id>', views.eliminarInscripcion),
    path('actualizarI/<int:id>',views.actualizarInscripcion),
]
