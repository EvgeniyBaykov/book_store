from django.urls import path
from app_market import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('book/<int:pk>/', views.BookView.as_view(), name='book'),
    path('catalog/', views.CatalogView.as_view(), name='catalog'),
]
