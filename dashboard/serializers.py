from rest_framework import serializers
from dashboard.models import Utilization

class UtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilization
        fields = '__all__'


