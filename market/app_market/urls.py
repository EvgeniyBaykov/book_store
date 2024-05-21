from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/<int:pk>/', views.BookView.as_view(), name='book'),
]
