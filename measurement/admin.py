from django.contrib import admin
from .models import Measurement, Sensor
# Register your models here.

@admin.register(Sensor)
class AdminSensor(admin.ModelAdmin):
    pass

@admin.register(Measurement)
class AdminMeasurement(admin.ModelAdmin):
    pass