"""ihujuu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from modulo1.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
     #--------------------------------------login--------------------------------#
  
    path('', ListadoEvento.as_view(template_name = "index.html"), name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='login.html'), name="logout"),
    #----------------------------login-----------------------------------------------#
    path('admin/', admin.site.urls),
    path('modulo1/',include(('modulo1.urls','modulo1'))),
    path('home/', Home1, name= 'index3'),
    #------------------------------------------registro----------------------------#
    path('ccionpermitida/', ListadoAccionpermitida.as_view(template_name = "crud\ccionpermitida\index.html"), name='leerccion'),
    path('discografia/', Discografia, name='discografia'),
    path('registro/', registro_usuario, name='registro_usuario'),
#------------------------------------------registro----------------------------#
#------------------------------------------recuperacion----------------------------#


#------------------------------------------recuperacion----------------------------#    
    
]
