from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .forms import PostForm
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

# create a new post
def create_post_view(request, *args, **kwargs):
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
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