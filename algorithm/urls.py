from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name="algorithm"

urlpatterns = [
    path('', views.home, name="homepage"),
    path('submitted/', views.submitted, name="submitted")
    # path('single/<slug:slug>', views.single, name="single"),
    # path('aboutus/', views.aboutus, name="aboutus"),
]