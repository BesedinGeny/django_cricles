from django.shortcuts import render, redirect
from .models import Circle
from .forms import CircleForm
# Create your views here.


def index(request):
    if request.method=="POST":
        form = CircleForm(request.POST)
        form.save()
        return redirect('/')
    form = CircleForm()
    dict = {'title': 'Вывод', 'form': form}
    return render(request, 'main/index.html', dict)


def result(request):
    circles = Circle.objects.all()
    return render(request, 'main/result.html', {'title': 'Вывод', 'circles' : circles})