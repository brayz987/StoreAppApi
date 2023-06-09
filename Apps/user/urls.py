from django.urls import path, include
from .views import RegisterUserView,InformationUserView,PasswordUserView

urlpatterns = [
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path(r'register/', RegisterUserView.as_view(), name='auth_register'),
    path(r'', InformationUserView.as_view(), name='users'),
    path(r'updatePassword', PasswordUserView.as_view(), name='password')
]