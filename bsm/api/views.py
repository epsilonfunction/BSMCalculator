from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SampleItem,BSMCalculation
from .serializers import SampleItemSerializer,BSMCalculationSerializer


class SampleItemView(APIView):
    def get(self, request):
        items = SampleItem.objects.all()
        serializer = SampleItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = SampleItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class BlackscholesView(APIView):

    def get(self, request):
        items = BSMCalculation.objects.all()
        serializer = BSMCalculationSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BSMCalculationSerializer(data=request.data)
        if serializer.is_valid():
            ressults= serializer.calculate()
            return Response(ressults, status=201)
        return Response(serializer.errors, status=400)


from django.shortcuts import render


# Create your views here.
