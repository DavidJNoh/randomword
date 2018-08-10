from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

  # the index function is called when root is visited
def index(request):    
    data = {
        'word': get_random_string(length=14)
    }
    if 'count' not in request.session:
        request.session['count'] = 0

    request.session['count'] += 1

    return render(request,'randomword/index.html', data)
