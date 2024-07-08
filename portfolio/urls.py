from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
]