from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.conf import settings
from .forms import PostForm
from .models import Post
from django.core.exceptions import PermissionDenied

# home page
def home_view(request, *args, **kwargs):
    return render(request, "pages/welcome.html", context={})

def home_view_posts(request, *args, **kwargs):
    return render(request, "pages/home.html", context={})

# post tweet view
def posts_list_view(request, *args, **kwargs):
    allPosts = Post.objects.all()
    posts_list = [post.serialize() for post in allPosts]
    data = {
      "response": posts_list
    }
    return JsonResponse(data)

# create a new post
def create_post_view(request, *args, **kwargs):
    form = PostForm(request.POST)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()
        if request.is_ajax():
            return JsonResponse(post.serialize())
        if next_url != None:
            return redirect(next_url)
        form = PostForm()
    return render(request, 'components/form.html', context={"form": form})

# post detail view
def post_detail_view(request, post_id, *args, **kwargs):
    data = {
      "id": post_id,
    }
    try:
        obj = Post.objects.get(id=post_id)
        data['content'] = obj.content
    except:
        data['message'] = "Post not found"
    return JsonResponse(data)