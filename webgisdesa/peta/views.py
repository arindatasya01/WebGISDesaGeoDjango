from django.shortcuts import render, redirect
from .models import Superhero
from django.contrib import messages

# Create your views here.
# View untuk READ
def LihatSuperhero(request):
    SemuaHero = Superhero.objects.all()

    context ={
        'Semua_Hero': SemuaHero,
    }

    return render (request, "peta/index.html", context)

# View untuk CREATE
def createSuperhero(request):
    return render(request, 'peta/create.html')

def simpan(request):
    hero = Superhero() #nama kelas di models.py
    hero.nama = request.POST.get('nama') #nama kolom di models.py
    hero.lat = request.POST.get('lat')
    hero.long = request.POST.get('long')
    hero.asosiasi = request.POST.get('asosiasi')
    hero.save()
    messages.success(request, "Superhero baru berhasil ditambahkan!")
    return redirect('/peta/create')

# View untuk DELETE
def deleteSuperhero(request, id):
    hero = Superhero.objects.get(id = id)
    hero.delete()
    messages.success(request, "Superhero berhasil dihapus")
    return redirect('/peta')

# Views untuk UPDATE SUPERHERO
def updateSuperhero(request,id):
    hero = Superhero.objects.get(id = id)
    return render(request, 'peta/update.html',{'hero':hero})
    
# Views untuk UPDATE
def update(request, id):
    hero = Superhero.objects.get(id = id)
    hero.nama = request.POST.get('nama') #nama kolom di models.py
    hero.lat = request.POST.get('lat')
    hero.long = request.POST.get('long')
    hero.asosiasi = request.POST.get('asosiasi')
    hero.save()
    messages.success(request, "Superhero berhasil diupdate!")
    return redirect('/peta')
