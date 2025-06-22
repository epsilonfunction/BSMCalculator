from rest_framework import serializers
from .models import SampleItem, BSMCalculation
from .quant.blackscholes import blackscholes


# Serializers convert database model into JSON format 
# Deserializers convert JSON data, validates it, converts back into database model

class SampleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleItem
        fields = '__all__'  # This will include all fields in the model
        # Alternatively, you can specify the fields explicitly:

class BSMCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BSMCalculation
        fields = [
            'S',
            'K',
            't',
            'r',
            'q',
            'sigma'
        ]
    
    def calculate(self):
        print('starting calculate')
        bs = blackscholes(
            S=self.validated_data['S'],
            K=self.validated_data['K'],
            t=self.validated_data['t'],
            r=self.validated_data['r'],
            sigma=self.validated_data['sigma']
        )
        print('ending calculate')


        return {
            'call_price': bs.Call(),
            'put_price': bs.Put(),
            'call_delta': bs.get_delta()[0],
            'put_delta': bs.get_delta()[1],
            'gamma': bs.get_gamma()
        }
