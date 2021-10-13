from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Images

from .serializers import ImageSerializers

class ImageView(APIView):
    def get(self, request, format=None):
        image = Images.objects.filter(status='SITE')
        serializer = ImageSerializers(image, many=True)
        return Response(serializer.data)