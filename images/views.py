from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from .models import Images
from .serializers import (
    ImagesSerializer, 
)


class ImagesListCreateView(APIView):
    def get(self, request, format=None):
        images = Images.objects.filter(status='GALLERY')
        serializer = ImagesSerializer(images, many=True)
        return Response(serializer.data)