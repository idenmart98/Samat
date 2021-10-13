from django.shortcuts import render
from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Images
from .serializers import (
    ImagesSerializer, 
    )
class ImagesListCreateView(APIView):
    def get(self, request, format=None):
        images=Images.objects.all()
        serializer = ImagesSerializer(images, many=True)
        return Response(serializer.data)
# Create your views here.
