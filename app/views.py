from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import pandas as pd
from .models import Tree

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def homepage(request):
    return render(request, 'homepage.html')

def showdata(request):
    df = pd.read_csv('TreeSpecies.csv')
    for index, row in df.iterrows():
        tree = Tree(
            tree_id=row['TreeID'],
            species=row['Species'],
            form=row['form'],
            growth_rate=row['growth_rate'],
            fall_color=row['fall_color'],
            environmental_tolerances=row['environmental_tolerances'],
            location_tolerances=row['location_tolerances'],
            notes_suggested_cultivars=row['notes_suggested_cultivars'],
            tree_size=row['tree_size'],
        )
        tree.save()
    trees = Tree.objects.all()
    return render(request, 'showdata.html', {'trees': trees})

