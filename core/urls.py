from django.urls import path
from .views import Register, MeView

urlpatterns = [

    path('register/', Register.as_view(), name='register'),
    path('me/', MeView.as_view(), name='profile')
]