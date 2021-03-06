"""app_jing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administracion/', include('Administration.urls')),
    path('partidos/', include('Match.urls')),
    path('equipos/', include('Team.urls')),
    path('', include('News.urls')),
    path('personas/', include('Person.urls')),
    path('mensajes/', include('Message.urls')),
    path('sport/', include('Sport.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
