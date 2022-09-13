from hashlib import new
import mailbox
from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import render
from .models import User
# Create your views here.

def home(request):
    return HttpResponse("Listado de estudiantes")

def index(request):
    return render(request, 'index.html')

def new_user(request):
    if request.method == 'POST':
        username= request.POST["user"]
        name = request.POST["name"]   
        mail = request.POST["mail"]
        password = request.POST["psw"]
        birthdate = request.POST["bithdate"]
        new_user = User(username, name, mail, password, birthdate)
    