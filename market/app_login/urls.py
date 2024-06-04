from django.urls import path
from app_login.views import (LogView,
                             LogoutUserView,
                             UserResetPasswordView,
                             UserPasswordResetDoneView,
                             UserPasswordResetConfirmView,
                             UserPasswordResetCompleteView,
                             register_view,
                             UserDeleteView,
                             )

urlpatterns = [
    path('login/', LogView.as_view(), name='login'),
    path('registration/', register_view, name='registration'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('password-reset/', UserResetPasswordView.as_view(), name='password_reset'),
    path('password-reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('delete-account/', UserDeleteView.as_view(), name='delete_account'),
]
