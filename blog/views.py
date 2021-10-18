from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post

from .serializers import PostSerializers

class PostView(APIView):
    def get(self, request, format=None):
        status = Post.objects.filter(status='SITE')
        serializer = PostSerializers(status, many=True)
        return Response(serializer.data)