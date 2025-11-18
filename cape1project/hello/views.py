from django.shortcuts import render   
from django.http import HttpResponse,HttpResponseForbidden,HttpResponseNotFound,HttpResponseBadRequest,JsonResponse

def index(request):
    return JsonResponse({"products": "banana", "other products": "milk"})

def contact_us(request):
    return HttpResponse("<h1>contact-us: +7 700 248 75 68</h1>")

def notfound_404(request, exception):
    return HttpResponseNotFound("<h1>Такой страницы несуществует </h1>")

def set_cookie(request):
    username=request.GET.get("username","Undefined")
    response= HttpResponse(f"HEllo {username}")
    response.set_cookie("username", username)
    return response

    








# def index(request):
#     return HttpResponse('<h1>Блог по Python</h1>')

# def list(request):
#     id_s=request.GET.get('id')

#     if id_s == "1":
#         return HttpResponse("<h1>Статья 1: Введние</h1>")
#     elif id_s == "2":
#         return HttpResponse("<h1>Статья 2: Основаня часть</h1>")
#     elif id_s == "3":
#         return HttpResponse("<h1>Статья 3: Заключение</h1>")
#     else:
#         return HttpResponse("""
#             <h1>Список статей</h1>
#             <ul><li>1—Введние</li><li>2—Основаня часть</li><li>3—Заключение </li></ul>""")
# def news(request):
#     return HttpResponse("<h1>Новости</h1><p>Сегодня был всемирный день Python.</p>")

# def artdetail(request, article_id):
#     return HttpResponse(f'<h1> Статья{article_id}</h1>')
    
# def list(request,id):
#     return HttpResponse(f"All articles: Статья №1\nСтатья №2\nСтатья №3 ")

# def article(request, id):
#     return HttpResponse(f"article ID:{id} ")

# def news(request,id):
#     return HttpResponse(f"News ID:{id} \n Сегодня в Алматы произошел великолепный фестиваль в честь 3 дня рождения Майкрасофт. В связи с этим событием несколько участников мероприятия были вознаграждены медальями за отвагу Microsoft ")
    
# def article1(request,id):
#     id==1 
#     return HttpResponse(f"Статья 1: Введение в Пайтон")

# def article2(request,id):
#     id==1 
#     return HttpResponse(f"Статья 2: Основная часть ")

# def article3(request,id):
#     id==1 
#     return HttpResponse(f"Статья 3: Заключение ")

    
#   return HttpResponse("Hello green",headers={"sECRETcODE":"123444"})
# def request_info(request):
#     method=request.method
#     path=request.path
#     user_agent=request.headers.get('User_agent')
#     host= request.get_host()

#     response_content=f'Method    :{method}Path:{path}    Brauzer:{user_agent}     Host:{host}'
#     response = HttpResponse(response_content, content_type="text/plain")
#     response['Secret-Code']= "Erasyl"
#     return response

# def show_info(request,username):
#     return HttpResponse(f'Профиль пользователя: {username}')

# def about_detail(request,code=None):
#     if code:
#         return HttpResponse(f"абоут: {code}")
#     else:
#         return HttpResponse("абоут")

# def contact(request):
#     return render(request, 'contact.html')

# def tovar_detail(request,id):
#     tovars={1: {'name': 'МЕРС'},
#             2: {'name': 'АУДИ'}, 
#             3: {'name': 'ЛЕКСУС'} }
#     tovar=tovars.get(id)
#     if tovar is None:
#         return render(request, 'ne_naideno.html', {'id': id})

#     return render(request, 'tovar_detail.html', {'product': tovar})
