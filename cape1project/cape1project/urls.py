from django.contrib import admin
from django.urls import path, re_path,include
from hello import views

# blog_patterns=[path("", views.list), path("<int:article_id>/", views.artdetail), path("news/", views.news)]

urlpatterns = [
    path('index', views.index, name='home'),
    path("contact-us/", views.contact_us),
    path("set_cookie", views.set_cookie)
   
    
    # path('info/<str:username>/', views.show_info ),
#     path('tovar/<int:id>/', views.tovar_detail, name="tovar_detail"),
#     re_path(r'^about/(?P<code>[A-Za-z0-9]+)?/?$', views.about_detail, name="about_detail"),
#     path('contact/', views.contact, name='contact'),
#     path('admin/', admin.site.urls),
]
error404='cape1project.views.notfound_404'
