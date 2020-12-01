from django.contrib import admin
from django.urls import path

from posts.views import (
    home_view, 
    post_detail_view, 
    posts_list_view, 
    create_post_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('create-post/', create_post_view),
    path('posts/', posts_list_view),
    path('posts/<int:post_id>', post_detail_view)
]
