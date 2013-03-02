from django.http import Http404
from django.shortcuts import render_to_response
from blog.models import Post

def blog(request):
    posts = Post.objects.all()
    left = [p for p in posts if p.id % 2 == 1]
    right = [p for p in posts if p.id % 2 == 0]
    return render_to_response('blog.html', {'left': left,
                                            'right': right})

def post(request, num):
    try:
        n = int(num)
        if n < 1 or n > Post.objects.count():
            raise Http404()
    except ValueError:
        raise Http404()
    p = Post.objects.get(id=n)
    return render_to_response('post.html', {'p': p})


