from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError

class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'

    def validate_litr(self, value):
        if value > 19:
            raise ValidationError("Bunday katta litrlarda suv sotilmaydi")
        else:
            return value

class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'

class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'

class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'

    def validate_mijoz_id_qarz(self, value):
        if value > 500000:
            raise ValidationError("Qarzingiz juda ko’p, buyurtma qilolmaysiz!")
        else:
            return value