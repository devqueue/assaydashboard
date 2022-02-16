from rest_framework import serializers
from dashboard.models import Utilization, Samples, Revenue, MissedRevenue



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


class MissedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissedRevenue
        fields = '__all__'


