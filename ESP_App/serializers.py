from rest_framework.serializers import ModelSerializer

from ESP_App.models import Esp_data


class ESP_DataSerializer(ModelSerializer):
    class Meta:
        model = Esp_data
        fields = ('temperature', 'humidity', 'save_date')
