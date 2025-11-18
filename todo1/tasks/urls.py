from django.urls import path
from . import views
from django.views.generic import  TemplateView

urlpatterns=[
    path('',views.index),
    # path('about/',TemplateView.as_view(template_name="about.html",
    #                                    extra_context={"header":"CSS company"})),
    # path('contacts/',TemplateView.as_view(template_name="contact.html",
    #                                    extra_context={"header":"about us: +7 006 451 4920"})),
#     path('tasks/<int:task_id>/', views.view_task,name='view_task'),
#     path('task/new/', views.create_task,name='create_task'),
#     path('tasks/<int:task_id>/edit', views.edit_task,name='edit_task'),
#     path('tasks/<int:task_id>/delete', views.delete_task,name='delete_task'),
]