from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CurrenciesConverterView, CurrenciesView

router = DefaultRouter()
router.register(r'currencies', CurrenciesView, basename='currency')
urlpatterns = router.urls
urlpatterns.append(path('convert/', CurrenciesConverterView.as_view()))
