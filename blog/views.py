from django.http import Http404
from django.shortcuts import render_to_response
from blog.models import Post

def blog(request):
    posts = Post.objects.all()
    return render_to_response('blog.html', {'posts': posts})

def post(request, num):
    try:
        n = int(num)
        if n < 1 or n > Post.objects.count():
            raise Http404()
    except ValueError:
        raise Http404()
    p = Post.objects.get(id=n)
    return render_to_response('post.html', {'p': p})


