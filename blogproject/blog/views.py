from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

def article_list(request):
    articles=Article.objects.all().order_by('-timestamp')
    return render(request,'artlist.html',{'articles':articles})

def artdetail(request,id):
    article=get_object_or_404(Article, id=id)
    return render(request,'artdetail.html',{'article':article})
    
@login_required
def artcreate(request):
    if request.method == "POST":
        form=ArticleForm(request.POST)
        if form.is_valid():
            article=form.save(commit=False)
            article.user=request.user
            article.save()
            return redirect('artlist')
    else:
        form= ArticleForm()
    return render(request,'artcreate.html',{'form':form})
        
@login_required        
def artedit(request, id):
    article=get_object_or_404(Article,id=id)
    if article.user!=request.user:
        return redirect('artlist')
    if request.method=='POST':
        form=ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('artlist')
    else:
        form=ArticleForm(instance=article)
    return render(request,'artedit.html',{'form':form, 'article':article})
    
@login_required    
def artdelete(request,id):
    article=get_object_or_404(Article,id=id)
    if article.user==request.user:
        article.delete()
    return redirect('artlist')

def login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("artlist")
        else:
            return render(request,"login.html",{"error":"Неправильные  данные"})
    return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def register_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return render(request,"register.html",{"error":"Имя используется"})
        user=User.objects.create_user(username=username, password=password)
        return redirect("login")
    return render(request,"register.html")