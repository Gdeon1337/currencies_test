from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Currencies
from .serializers import CurrenciesSerializer

from rest_framework import viewsets


class CurrenciesView(viewsets.ModelViewSet):
    serializer_class = CurrenciesSerializer
    queryset = Currencies.objects.all()


class CurrenciesConverterView(APIView):
    def get(self, request):
        base_currency_id = request.query_params.get('base_currency_id')
        convert_currency_id = request.query_params.get('convert_currency_id')
        count = request.query_params.get('count', 1)
        base_currency = get_object_or_404(Currencies.objects.all(), pk=base_currency_id)
        convert_currency = get_object_or_404(Currencies.objects.all(), pk=convert_currency_id)
        currency_rate = (base_currency.ruble_rate / convert_currency.ruble_rate) * float(count)
        return Response({
            'base_currency': {
                'title': base_currency.title,
                'count': count
            },
            'convert_currency': {
                'title': convert_currency.title,
                'count': round(currency_rate, 2)
            }
        })
