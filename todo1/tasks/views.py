from django.shortcuts import render,redirect,get_object_or_404
# from .models import Task
# from django.core.paginator import Paginator
# from django.template.response import TemplateRespons
from django.http import HttpResponse
from .forms import UserForm

def index(request):
    userform=UserForm()
    if request.method=="POST":
        userform=UserForm(request.POST)
        if userform.is_valid():
            name=userform.cleaned_data['name']
            email=userform.cleaned_data['email']
            password=userform.cleaned_data['password']
            return HttpResponse(f'Hello{name}, your email is   {email}, and u r password is {password} ')
    return render(request,'index.html',{"form":userform})
    
    
    
    
    
    
    
    
    
    
#    if request.method=="POST":
#        form=UserForm(request.POST)
#        if form.is_valid():
#             name=request.POST.get('name')
#             age=request.POST.get('age')
#             # lang=request.POST.get('lang')
#             # return HttpResponse(f'Hello {name} Your age is: {age} ur languages is: {lang}')
#    else:
#        form=UserForm()
#        return render(request,'index.html',{'form':form})




# def index(request):
#     sort=request.GET.get('sort','new')
#     if sort=='old':
#         tasks=Task.objects.all().order_by('created_at')
#     else:
#         tasks=Task.objects.all().order_by('-created_at')
#     paginator=Paginator(tasks,3)
#     page_num=request.GET.get('page')
#     page_obj=paginator.get_page(page_num)
#     return render(request,'tasks/index.html',{'tasks': page_obj, 'page_obj': page_obj, 'sort': sort})

# def view_task(request,task_id):
#     task=get_object_or_404(Task,pk=task_id)
#     return render(request,'tasks/view_task.html',{'task':task})

# def create_task(request):
#     if request.method=="POST":
#         title=request.POST['title']
#         description=request.POST.get('description','')
#         Task.objects.create(title=title,description=description)
#         return redirect('index')
#     return render(request,'tasks/create_task.html')
    
# def edit_task(request,task_id):
#     task=get_object_or_404(Task,pk=task_id) 
#     if request.method=="POST":
#         title=request.POST['title']
#         description=request.POST.get('description','')
#         task.completed='completed' in request.POST    
#         task.save()
#         return redirect('index')
#     return render(request,'tasks/edit_task.html',{'task':task})
        
# def delete_task(request,task_id):
#     task=get_object_or_404(Task,pk=task_id)
#     if request.method=='POST':
#         task.delete()
#         return redirect('index')
#     return render(request,'tasks/delete_task.html',{'tasks':task})    
    
    
    
    
    



