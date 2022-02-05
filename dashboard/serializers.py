from rest_framework import serializers
from dashboard.models import Utilization
from dashboard.models import Processed
from dashboard.models import Revenue



class UtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilization
        fields = '__all__'


class ProcessedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processed
        fields = '__all__'


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'


