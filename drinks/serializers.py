from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    image= serializers.ImageField(required=False)
    class Meta:
        model = Drink 
        fields=['id','name','description','image']
