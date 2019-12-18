"""jango_currencies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from currencies_api.views import CurrenciesConverterView, CurrenciesView

router = DefaultRouter()
router.register(r'currencies', CurrenciesView, basename='currency')
urlpatterns = router.urls
urlpatterns.append(path('admin/', admin.site.urls))
urlpatterns.append(url(r'^auth/', include('rest_auth.urls')))
urlpatterns.append(url(r'^auth/registration/', include('rest_auth.registration.urls')))
urlpatterns.append(path('converter/', CurrenciesConverterView.as_view()))
