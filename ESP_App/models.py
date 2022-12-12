from django.db import models


# Create your models here.
class Esp_data(models.Model):
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    save_date = models.DateTimeField(auto_now_add=True, null=True)
