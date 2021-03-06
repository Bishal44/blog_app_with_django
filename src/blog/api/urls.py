from blog.api.views import (api_detail_blog,
api_update_blog_view,
	api_delete_blog_view,
	api_create_blog_view,
)
from django.urls import path


app_name = 'blog'
urlpatterns = [

    path('<slug>/', api_detail_blog, name="detail"),
    path('<slug>/update', api_update_blog_view, name="update"),
	path('<slug>/delete', api_delete_blog_view, name="delete"),
	path('create', api_create_blog_view, name="create"),

]