from django.http import Http404
from django.shortcuts import render_to_response
from blog.models import Post

def blog(request):
    posts = Post.objects.all()
    pcols = [[],[]]
    for (i, p) in enumerate(posts):
        pcols[i % 2].append(p)
    return render_to_response('blog.html', {'lposts': pcols[0],
                                            'rposts': pcols[1]})

def post(request, num):
    try:
        n = int(num)
        if n < 1 or n > Post.objects.count():
            raise Http404()
    except ValueError:
        raise Http404()
    p = Post.objects.get(id=n)
    return render_to_response('post.html', {'p': p})


