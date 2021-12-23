from django.urls import path
from. import views
urlpatterns=[
    path('',views.todoindex,name='todoindex'),
    path('delete/<str:pk>',views.delete,name='delete')
] 