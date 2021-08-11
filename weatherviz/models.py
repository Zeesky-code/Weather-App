from django.db import models
from django.utils.translations import gettext_lazy as _


class OpenWeatherCity(models.Model):
    name = models.CharField(
        verbose_name=_('City Name'),
        max_length=150, null=False, blank=False
        )
    country = models.CharField(
        verbose_name=_('Country'),
        max_length=10, null=False, blank=False
        )
    open_weather_id = models.IntegerField(
        verbose_name=_('Open Weather ID'),
        null=False, blank= False
        )

    class Meta:
        verbose_name=_('Open Weather City')
        verbose_name_plural=_('Open Weather Cities')