from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  blog.models import BlogPost
from blog.api.serializers import BlogPostSerializer
@api_view(['GET',])
def api_detail_blog(request,sl):
    try:
        blogpost=BlogPost.objects.get(sl)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
