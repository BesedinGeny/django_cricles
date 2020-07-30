from django.shortcuts import render, redirect
from .models import Circle
from .forms import CircleForm
from .services import paint, clear
import time
# Create your views here.


def index(request):

    if request.method=="POST":
        form = CircleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = CircleForm()
    dict = {'title': 'Вывод', 'form': form}
    return render(request, 'main/index.html', dict)


def result(request):
    if request.method=="POST":
        if "_paint" in request.POST:
            paint()
            # несмотря на то, что отрисовка идет долго
            # страница обновляется быстро и картинка
            # не успевает загрузиться
            time.sleep(0.5)
            return redirect('/result')
        elif "_clear" in request.POST:
            clear()
            return redirect('/result')

    circles = Circle.objects.all()
    return render(request, 'main/result.html', {'title': 'Вывод', 'circles' : circles})