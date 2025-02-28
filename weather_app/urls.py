from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('yearly-report/', views.yearly_report, name='yearly_report'),
]