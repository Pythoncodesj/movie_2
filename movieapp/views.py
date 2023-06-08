from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Movie
from .forms import Modelform

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }

    return render(request,'index.html',context)


def detail(request,movie_id):
    # return HttpResponse("this is movie app" % movie_id)
    movie=Movie.objects.get(id=movie_id)

    return render(request,'details.html',{'movie':movie})


def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year= request.POST.get('year')
        img = request.FILES['img']
        s = Movie(name=name, desc=desc, img=img, year=year)
        s.save()
        print("movie  added")
    return render(request,"add.html")



def update(request, id):
    movie = Movie.objects.get(id=id)
    form = Modelform(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form, 'movie': movie})


def delete(request,id):
    if request.method=='POST':
        obj=Movie.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')
