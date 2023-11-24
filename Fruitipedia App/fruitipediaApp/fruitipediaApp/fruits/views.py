from django.shortcuts import render, redirect, get_object_or_404

from fruitipediaApp.fruits.forms import FruitCreateForm, CategoryCreateForm
from fruitipediaApp.fruits.models import Fruit, Category


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()
    context = {
        'fruits': fruits
    }
    return render(request, 'common/dashboard.html', context)


def fruit_create(request):
    form = FruitCreateForm()
    if request.method == "POST":
        form = FruitCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
    }

    return render(request, 'fruits/create-fruit.html', context)


def create_category(request):
    form = CategoryCreateForm()
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dashboard page')

    context = {
        'form': form,
    }
    return render(request, 'categories/create-category.html', context)


def fruit_details(request, fruit_pk):
    fruit = get_object_or_404(Fruit, pk=fruit_pk)
    context = {
        'fruit': fruit
    }
    return render(request, 'fruits/details-fruit.html', context)


def edit_details(request, fruit_pk):
    fruit = get_object_or_404(Fruit, pk=fruit_pk)

    form = FruitCreateForm(instance=fruit)

    if request.method == "POST":
        form = FruitCreateForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
    }

    return render(request, 'fruits/edit-fruit.html', context)


def delete_details(request, fruit_pk):
    fruit = get_object_or_404(Fruit, pk=fruit_pk)

    form = FruitCreateForm(instance=fruit)

    if request.method == "POST":
        form = FruitCreateForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        'form': form,
        'fruit': fruit
    }
    return render(request, 'fruits/delete-fruit.html')
