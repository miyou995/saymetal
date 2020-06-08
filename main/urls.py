
from django.urls import path, include 
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import HomeView, ProductListView, ReferencesListView, ContactFormView




urlpatterns = [
    # path('', HomeView.as_view(), name='index'),
    path('', views.home, name='index'),
    path('produits/', ProductListView.as_view(), name='products'),
    path('about/', ReferencesListView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]
