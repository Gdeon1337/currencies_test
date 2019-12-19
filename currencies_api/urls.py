from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CurrenciesConverterView, CurrenciesView

router = DefaultRouter()
router.register(r'currencies', CurrenciesView, basename='currency')
urlpatterns = router.urls
urlpatterns.append(path('admin/', admin.site.urls))
urlpatterns.append(url(r'^auth/', include('rest_auth.urls')))
urlpatterns.append(url(r'^auth/registration/', include('rest_auth.registration.urls')))
urlpatterns.append(path('convert/', CurrenciesConverterView.as_view()))
