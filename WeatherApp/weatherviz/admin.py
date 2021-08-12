from django.contrib import admin
from weatherviz.models import OpenWeatherCity


class OpenWeatherCityAdmin(admin.ModelAdmin):
    pass

admin.site.register(OpenWeatherCity, OpenWeatherCityAdmin)
