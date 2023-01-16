from django.urls import path
from .views import SignUpView
from django.contrib.auth.forms import PasswordChangeForm
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
