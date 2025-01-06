from django.urls import path
from . import views

urlpatterns=[
    path('',views.Master.as_view(),name='master'),
    path('detail/<int:pk>',views.Detail.as_view(),name='detail')
]