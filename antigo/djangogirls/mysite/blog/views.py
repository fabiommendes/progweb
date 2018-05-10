from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, 'post_list.html', {'posts': posts})
    

class Foo:
    ham = 'spam'
    
    def answer(self):
        return 42

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    ctx = {
        'post' : post,
        'my_dict': {'foo': 'bar', 'answer': 42},
        'foo': Foo()
    }
    return render(request, 'post_detail.html', ctx)
