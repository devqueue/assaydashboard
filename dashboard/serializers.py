from rest_framework import serializers
from dashboard.models import Utilization

class UtilizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilization
        fields = ('AssayID',
                  'Assay',
                  'January',
                  'February',
                  'March',
                  'April',
                  'June',
                  'July',
                  'August',
                  'September',
                  'October',
                  'November',
                  'December',
                  'Year',
                  'MonthlyIndex',
                  )



