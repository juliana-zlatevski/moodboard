from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Post

# Create your views here.
def home_view(request, *args, **kwargs):
  return HttpResponse("<h1>Home View</h1>")

def post_detail_view(request, post_id, *args, **kwargs):
  try:
    obj = Post.objects.get(id=post_id)
  except:
    raise Http404
  return HttpResponse(f"<h1>Hello {post_id} - {obj.content}</h1>")