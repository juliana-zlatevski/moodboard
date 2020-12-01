from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Post

# home page
def home_view(request, *args, **kwargs):
    return render(request, "pages/home.html", context={})

# post tweet view
def posts_list_view(request, *args, **kwargs):
    allPosts = Post.objects.all()
    posts_list = [{"id": post.id, "content": post.content} for post in allPosts]
    data = {
      "response": posts_list
    }
    return JsonResponse(data)

# post detail view
def post_detail_view(request, post_id, *args, **kwargs):
    data = {
      "id": post_id,
    }
    status = 200
    try:
        obj = Post.objects.get(id=post_id)
        data['content'] = obj.content
    except:
        data['message'] = "Post not found"
        status = 404
    return JsonResponse(data, status=status)