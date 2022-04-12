from asyncio.windows_events import NULL
from datetime import date
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import depence, recette
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    deps = depence.objects.all()
    recs = recette.objects.all()
    valeur_dep = 0.0
    valeur_rec = 0.0
    for dep in deps:
        valeur_dep= valeur_dep + dep.montant 
    for rec in recs:
        valeur_rec= valeur_rec + rec.montant 

    bienifice= valeur_rec - valeur_dep
    return render(request,'tpvapp/index.html',{"dep":deps,"rec":recs,"valeur":bienifice})


def index_filtred(request):
  
    if request.method == "POST" :
        print("postggfgfgfgfgfgffff")
        date1 = request.POST.get("date1")
        date2 = request.POST.get("date2")
        
            
        deps = depence.objects.filter(date__gte=date1, date__lte=date2)
        recs = recette.objects.filter(date__gte=date1, date__lte=date2)
        valeur_dep = 0.0
        valeur_rec = 0.0
        for dep in deps:
            valeur_dep= valeur_dep + dep.montant 
        for rec in recs:
            valeur_rec= valeur_rec + rec.montant 

        bienifice= valeur_rec - valeur_dep
        return render(request,'tpvapp/index.html',{"dep":deps,"rec":recs,"valeur":bienifice})
    else:
        print("geeeeeeetttt")
        deps = depence.objects.all()
        recs = recette.objects.all()
        
        valeur_dep = 0.0
        valeur_rec = 0.0
        for dep in deps:
            valeur_dep= valeur_dep + dep.montant 
        for rec in recs:
            valeur_rec= valeur_rec + rec.montant 

        bienifice= valeur_rec - valeur_dep
        return render(request,'tpvapp/index.html',{"dep":deps,"rec":recs,"valeur":bienifice})



def add_view(request):
    
    if request.method == "POST" :
        if request.POST.get("montant_rec") and request.POST.get("date1") and request.POST.get("rec_par"):
            montant_rec = request.POST.get("montant_rec")
            date_rec = request.POST.get("date1")
            rec_par= request.POST.get("rec_par")
            recette.objects.create(montant=float(montant_rec),date=date_rec,par=rec_par)
            return render(request,'tpvapp/add.html',{"etat":"Ajouté !"})
        elif request.POST.get("montant_dep") and request.POST.get("date2") and request.POST.get("desc") and request.POST.get("dep_par"):
            montant_dep = request.POST.get("montant_dep")
            date_dep = request.POST.get("date2")
            desc= request.POST.get("desc")
            dep_par= request.POST.get("dep_par")
            depence.objects.create(montant=float(montant_dep),date=date_dep,description=desc,par=dep_par)
            return render(request,'tpvapp/add.html',{"etat":"Ajouté !"})
        else:
            return render(request,'tpvapp/add.html',{"etat":"Veuillez saisir tout les champs !"})
    else:
        return render(request,'tpvapp/add.html',{"etat":""})       

def singup_view(request):
    def not_exist(username):
        res=False
        users = User.objects.all()
        for user in users:
            if user.username==username:
                res=True
        return res

    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('name'):
            username=request.POST.get('username')
            password=request.POST.get('password')
            name=request.POST.get('name')
            if not_exist(username):
                User.objects.create(username=username,password=password,first_name=name)
                return redirect('/')
            else:
                return render(request,'tpvapp/singup.html',{'message':'le username existe'})
        else:
             return render(request,'tpvapp/singup.html',{'message':'veuillez remplir tous les champs!'})

    else:
        return render(request,'tpvapp/singup.html',{'message':''})
    
    



def login_view(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password'):
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('stats/')  
            else:
                return render(request,'tpvapp/login.html',{'message':'erreur : résseyez'})      
        else:
            return render(request,'tpvapp/login.html',{'message':'veuillez remplir les champs'})

    else:
        return render(request,'tpvapp/login.html',{'message':''})

def logout_view(request):
    logout(request)
    return redirect('/')        