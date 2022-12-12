from rest_framework import viewsets
from ESP_App.models import Esp_data
from ESP_App.serializers import ESP_DataSerializer


class Esp_DataViewSet(viewsets.ModelViewSet):
    queryset = Esp_data.objects.all().order_by('save_date')
    serializer_class = ESP_DataSerializer

