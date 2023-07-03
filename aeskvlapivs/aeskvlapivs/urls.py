"""
URL configuration for aeskvlapivs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from expediente.urls import expediente_patterns
from registration import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include(expediente_patterns)),
    path('', include('core.urls')),
    #paths de auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('auth/settings', views.settings, name='settings'),
    path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    path('success', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)

