from . import views
from django.urls import path

urlpatterns = [
    path('', views.article_list,name='artlist'),
    path('article/<int:id>/',views.artdetail,name='artdetail'),
    path('article/create/',views.artcreate,name='artcreate'),
    path('article/<int:id>/edit/',views.artedit,name='artedit'),
    path('article/<int:id>/delete/',views.artdelete,name='artdelete'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register_view,name='register'),
]