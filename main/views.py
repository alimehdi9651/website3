from django.shortcuts import render, redirect
from .forms import recipe_form
from .models import recipe

# Create your views here.


def index(request):
    return render(request, 'index.html')

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