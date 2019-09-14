from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account.models import Account
from  blog.models import BlogPost
from blog.api.serializers import BlogPostSerializer


@api_view(['GET',])
def api_detail_blog(request,slug):
    try:
        blogpost=BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="GET":
        serializer=BlogPostSerializer(blogpost)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_blog_view(request,slug):
    try:
        blogpost=BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =="PUT":
        serializer=BlogPostSerializer(blogpost,data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["sucess"] = "update sucessfully"
            return Response(data=data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_blog_view(request,slug):
    try:
        blogpost=BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation=blogpost.delete()
        data = {}
        if operation:
            data["sucess"]="sucessfully deleted"
        else:
            data["failure"] = "fail to deleted"
        return Response(data=data)


@api_view(['POST',])
def api_create_blog_view(request):
    account = Account.objects.get(pk=1)
    blogpost=BlogPost(author=account)
    if request.method == "POST":
        serializer = BlogPostSerializer(blogpost, data=request.data)
        data={}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)