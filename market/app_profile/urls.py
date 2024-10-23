from django.urls import path

from app_profile.views import AccountView, ProfileView


urlpatterns = [
    path('', AccountView.as_view(), name="account"),
    path('profile/', ProfileView.as_view(), name='profile'),
]
