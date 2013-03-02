from django.shortcuts import render_to_response

def about(request):
    return render_to_response('about.html', {})

def resume(request):
    return render_to_response('resume.html', {})

def work(request):
    return render_to_response('work.html', {})
