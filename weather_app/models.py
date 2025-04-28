from django.db import models

# Create your models here.

class WeatherRecord(models.Model):
    Max_Temperature = models.FloatField(null=True,blank=True)
    Min_Temperature=models.FloatField(null=True,blank=True)
    Humidity=models.IntegerField(null=True,blank=True)
    Max_Humidity=models.IntegerField(null=True,blank=True)
    Min_humidity = models.IntegerField(null=True,blank=True)


def __str__(self):
    return f"Weather on {self.date}"