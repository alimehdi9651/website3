from django.shortcuts import render, redirect
from .forms import recipe_form
from .models import recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login, logout
# Create your views here.


def index(request):
    return render(request, 'index.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"{first_name=}, {last_name=},{username=}")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register_page')
        
        user = User(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)  
        user.save()
        messages.info(request,"Account created sucessfully")
        return redirect('register_page')
    return render(request, 'register.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        if not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid username")
            return redirect('login_page')
        user = authenticate(request, username = username, password = password)
        if user :
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Incorrect Password")
            return redirect('login_page')
           
    return render(request, 'login.html')



def add_recipes(request):
    form = recipe_form()
    if request.method == 'POST':
        form = recipe_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_recipes')
        
    return render(request, 'Recipe/add_recipes.html', {
        'form':form
    })

def view_recipes(request):
    recipes = recipe.objects.all()
    return render(request, 'Recipe/view_recipes.html', {
        'recipes': recipes,
    })

def delete_recipes(request, id):
    reci = recipe.objects.get(id=id)
    reci.delete()
    return redirect('view_recipes')

def edit_recipes(request, id):
    reci = recipe.objects.get(id=id)
    form = recipe_form(instance=reci)
    if request.method == 'POST':
        form = recipe_form(request.POST, request.FILES, instance=reci)
        if form.is_valid():
            form.save()
            return redirect('view_recipes')
    return render(request,'Recipe/edit_recipies.html', {
        'form': form
    } )