from django.urls import path

from .views import (
    email_register, 
    confirm_email,
    user_login,
    request_password_reset,
    set_new_password,
    # SetNewPasswordAPIView,
    # LogoutAPIView,

)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('auth/email_register', email_register, name="email_register"),
    path('auth/confirm_email/<str:code>/', confirm_email, name="confirm_email"),
    path('auth/login/', user_login, name="user_login"),
    # path('auth/logout/', LogoutAPIView.as_view(), name="logout"),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/request-reset-email/', request_password_reset,name="request_password_reset"),
    path('password-reset/<str:code>/',set_new_password, name='set_new_password'),
    
]
