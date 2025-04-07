from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_view(request):
    if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            if username == "satyam" and password == "admin":
                return render(request, "login.html", {"success": "Welcome!!"})
            else:
                return render(request, "login.html", {"error": "Invalid username or password"})

    return render(request, "login.html")