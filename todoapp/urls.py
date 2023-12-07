
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cbvindex/', views.Tasklistview.as_view(), name='cbvindex'),
    path('cbvdetails/<int:pk>/', views.Taskdetailview.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.Taskupdateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete')
   
]
