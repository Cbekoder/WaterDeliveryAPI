from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import *
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


class AdminListAPIView(ListAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class AdminRetrieveAPIView(RetrieveAPIView):
    serializer_class = AdminSerializer

    def get_object(self):
        obj = get_object_or_404(Admin, id=self.kwargs['pk'])
        return obj



class HaydovchiListAPIView(ListAPIView):
    queryset = Haydovchi.objects.all()
    serializer_class = HaydovchiSerializer

class HaydovchiRetrieveAPIView(RetrieveAPIView):
    serializer_class = HaydovchiSerializer

    def get_object(self):
        obj = get_object_or_404(Haydovchi, id=self.kwargs['pk'])
        return obj


