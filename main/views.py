from django.shortcuts import render, redirect
from .forms import recipe_form

# Create your views here.


def index(request):
    return render(request, 'index.html')

def add_recipes(request):
    form = recipe_form()
    if request.method == 'POST':
        form = recipe_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_recipes')
        
    return render(request, 'Recipe/add_recipes.html', {
        'form':form
    })