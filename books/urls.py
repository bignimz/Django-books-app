from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:id>', views.show, name='show'),
    path('review/', views.review, name='review'),
]