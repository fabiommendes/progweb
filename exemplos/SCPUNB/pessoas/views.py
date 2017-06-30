from django.shortcuts import render
from django.http import HttpResponse
from .bricks import page
from .models import Discipline

def index_view(request):
    disciplines_list = Discipline.objects.all()
    print(disciplines_list)
    ctx = {
        'disciplines_list': disciplines_list
    }
    print(ctx)
    return render(request, 'index.html', ctx)
    
    
def list_view(request):
    data = page()
    return HttpResponse(data.render())
    
    
def detail_view(request, id):
    discipline = Discipline.objects.get(code=id)
    class_rooms = discipline.class_rooms.all()
    ctx = {
        'discipline': discipline,
        'class_rooms': class_rooms,
    }
    data = page()
    return render(request, 'discipline.html', ctx)
    
