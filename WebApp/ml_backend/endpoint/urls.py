from django.urls import path
#Adding View
from . import views
urlpatterns = [
    path('', views.home),
    path('result.html', views.result),
]
