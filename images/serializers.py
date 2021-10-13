from .models import Images
from rest_framework import serializers 

class ImageSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Images
        fields = '__all__'