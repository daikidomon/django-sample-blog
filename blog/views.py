from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm


def index(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', ctx)


def detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {
        'post': post
    }
    return render(request, 'blog/detail.html', ctx)


def create(request):
    ctx = {}
    if request.method == 'GET':
        ctx['form'] = PostForm
        return render(request, 'blog/create.html', ctx)
    elif request.method == 'POST':
        Post.objects.create(title=request.POST.get('title', None),
                            content=request.POST.get('content', None),
                            image=request.FILES['image'],
                            create_at=timezone.now())
        return redirect(to='index')


def modify(request, pk):
    ctx = {}
    if request.method == 'GET':
        post = get_object_or_404(Post, id=pk)
        ctx['form'] = PostForm(instance=post)
        return render(request, 'blog/modify.html', ctx)
    if request.method == 'POST':
        post = Post(id=pk,
                    title=request.POST.get('title'),
                    content=request.POST.get('content'),
                    image=request.FILES['image'],
                    update_at=timezone.now())
        post.save()
        return redirect(to='detail', pk=pk)


def delete(request, pk):
    ctx = {}
    if request.method == 'GET':
        instance = get_object_or_404(Post, id=pk)
        ctx['instance'] = instance
        return render(request, 'blog/delete.html', ctx)
    if request.method == 'POST':
        Post.objects.filter(id=pk).delete()
        return redirect(to='index')
