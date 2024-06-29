from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    user = request.user
    return render(request, 'home/home.html', {'user' : user})