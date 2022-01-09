from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from .bl import create_memory, fetch_memories, get_avatar

def index(request):
    user = request.user
    if user.is_authenticated:
        memories = fetch_memories(user)
        return render(request, 'index.html', {
            'user': user,
            'avatar': get_avatar(user),
            'memories': memories
        })
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

def new_memory(request):
    err = ''
    user = request.user
    if request.method == 'POST':
        memo_name = request.POST["name"]
        comment = request.POST["comment"]
        lat = request.POST["lat"]
        long = request.POST["long"]
        if create_memory(user, memo_name, comment, lat, long):
            return HttpResponseRedirect(reverse("index"))
        err = 'This location can not be defined'
    return render(request, 'new_memory.html', {
        'user': user,
        'avatar': get_avatar(user),
        'error': err
    })
