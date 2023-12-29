from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from .serializers import *

class SuvModelViewSet(ModelViewSet):
    queryset = Suv.objects.all()
    serializer_class = SuvSerializer


class MijozModelViewSet(ModelViewSet):
    queryset = Mijoz.objects.all()
    serializer_class = MijozSerializer
    filter_backends = [SearchFilter]
    search_fields = ['ism', 'tel']

class BuyurtmaModelViewSet(ModelViewSet):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializer


class AdminModelViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def update(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class HaydovchiModelViewSet(ModelViewSet):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer


