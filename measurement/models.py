from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    
    name = models.CharField(max_length=50, verbose_name='Именование')
    description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Сенсор'

class Measurement(models.Model):
    
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateField(auto_now=True,verbose_name='Дата')
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return str(self.date)
    
    class Meta:
        verbose_name = 'Измерение'
    
