from rest_framework import serializers
from dashboard.models import Utilization, Samples, Revenue, MissedRevenue, stats, monthlystats



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


class statsSerializer(serializers.ModelSerializer):
    class Meta:
        model = stats
        fields = '__all__'


class monthlystatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = monthlystats
        fields = '__all__'


