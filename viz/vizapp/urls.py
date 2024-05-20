from django.urls import path
from . import views

urlpatterns = [
    path('example/',views.index,name = 'index'),
    path('update/<int:pk>',views.update,name = 'update'),
    path('delete_todo/<int:pk>',views.delete,name = 'delete')
]

