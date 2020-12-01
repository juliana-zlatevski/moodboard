from django import forms
from .models import Post

max_post_length = 280

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
