from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Currencies


class CurrencyResource(resources.ModelResource):
    class Meta:
        model = Currencies
        fields = ('title', 'ruble_rate')


class CurrencyAdmin(ImportExportModelAdmin):
    resource_class = CurrencyResource


admin.site.register(Currencies, CurrencyAdmin)
