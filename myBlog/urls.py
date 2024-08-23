from django.urls import path
from django.views.generic import RedirectView
from .views import post, index, about, contact, signup, login_view

urlpatterns = [
    path('', RedirectView.as_view(url='/login/', permanent=False)),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('home', index, name='home'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('contact/', contact, name='contact'),
]