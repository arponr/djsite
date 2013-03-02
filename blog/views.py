from django.shortcuts import render_to_response
from blog.models import Post

def blog(request):
    posts = Post.objects.all()
    left = [p for p in posts if p.id % 2 == 1]
    right = [p for p in posts if p.id % 2 == 0]
    return render_to_response('blog.html', {'left': left,
                                            'right': right})


