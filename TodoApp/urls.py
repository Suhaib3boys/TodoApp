from django.urls import path

from . import views

app_name = 'webapp'
urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    # path('detail', views.detail, name='index')
]
