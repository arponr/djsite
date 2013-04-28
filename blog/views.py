from django.http import Http404  
from django.shortcuts import render_to_response, get_object_or_404
from blog.models import Post, Category

def blog(request):
    return render_to_response('blog.html', 
                              {'posts': list(Post.objects.all()) * 5,
                               'cats': Category.objects.all()}) 

def category(request, sl):
    c = get_object_or_404(Category, slug=sl)
    return render_to_response('category.html', 
                              {'posts': c.post_set.all(),
                               'cats': Category.objects.all(),
                               'cur': c}) 

def post(request, sl):
    p = get_object_or_404(Post, slug=sl)
    return render_to_response('post.html', {'p': p})


