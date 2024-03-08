from django.urls import path
from meal_map import views

app_name = 'meal_map'

urlpatterns = [
    
    path('restaurants/', views.RestaurantListView, name='restaurant-list'),
    path('restaurants/<int:pk>/', views.RestaurantDetailView, name='restaurant-detail'),
    
    path('base/', views.base, name ='base'),
    path('login/', views.login, name='login'),
    path('homepage/', views.homepage, name='homepage')
    
    
]