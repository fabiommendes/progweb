from django.db import models
from django.utils import timezone
from django.contrib import admin
from django import forms
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect

register_admin = (lambda cls: admin.site.register(cls) or cls)


#
# Models
#
@register_admin
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        app_label = 'blog'

    def __str__(self):
        return self.title


#
# Forms
#
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


#
# URLS
#
urlpatterns = []


def route(url):
    def decorator(func):
        urlpatterns.append(path(url, func, name=func.__name__))
        return func
    return decorator


@route('')
def post_list(request):
    posts = (
        Post.objects
        .filter(published_date__lte=timezone.now())
        .order_by('published_date')
    )
    return render(request, 'blog/post_list.html', {'posts': posts})


@route('post/<int:pk>/')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@route('post/new/')
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@route('post/<int:pk>/edit/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})
