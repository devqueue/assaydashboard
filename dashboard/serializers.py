from rest_framework import serializers
from dashboard.models import Utilization
from dashboard.models import Samples
from dashboard.models import Revenue



class UtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilization
        fields = '__all__'


class SamplesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Samples
        fields = '__all__'


class RevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revenue
        fields = '__all__'


