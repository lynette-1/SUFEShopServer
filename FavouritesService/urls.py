from rest_framework import routers
from django.urls import include, path
from FavouritesService.views import FavouritesDetail

urlpatterns = [
    path('favouritesdetail/',FavouritesDetail.as_view()),
    
]