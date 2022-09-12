from django.shortcuts import render , redirect
from .forms import RegisterForm , loginForm , addform
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
from .models import Memories
# Create your views here.
def registerpage(request):
    f = RegisterForm()
    if request.method == "POST":
        f = RegisterForm(request.POST)
        if f.is_valid():
            f.save()
            new_user = authenticate(username=f.cleaned_data['username'],
                                    password=f.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return redirect("home")
        else:
            print(f.errors)
        
    data = {
        'form' : f
    }
    return render(request, "registerpage.html" , data)

def loginpage(request):
    f = loginForm()
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username , password = password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            print('invalid credentials')
    data = {
        'form' : f
    }
    return render(request, "login.html", data)

def logoutpage(request):
    logout(request)
    return redirect("loginpage")

@login_required(login_url='loginpage')
def home(request):
    objects = Memories.objects.filter(user=request.user)
    qwerty = request.GET.get('qwery')
    if qwerty is not None:
        objects = objects.filter(title__icontains = qwerty)
        print(objects)

    data = {
        'memory' : objects
    }
    return render(request, "home.html", data)


@login_required(login_url='loginpage')
def Addmemory(request):
    f = addform()
    if request.method == "POST":
        f = addform(request.POST)
        if f.is_valid():
            obj = f.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("home")
    data = {
        'form' : f
    }
    return render(request, "add.html", data)

@login_required(login_url='loginpage')
def edit_memory(request, slug):
    obj= Memories.objects.get(slug=slug)
    if obj.user == request.user:
        f = addform(initial={'title':obj.title, 'content': obj.content})
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']
            obj.title = title
            obj.content = content
            obj.save()
            return redirect("home")
    else:
        return redirect("home")
    return render(request, "edit.html", {
        'form': f
    })

@login_required(login_url='loginpage')
def delete_item(request,slug):
    obj = Memories.objects.get(slug=slug)
    if obj.user == request.user:
        obj.delete()
        return redirect("home")
        
        

