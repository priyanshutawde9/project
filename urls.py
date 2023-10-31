from django.urls import path
from FOLDER import views
from .views import move_to_bin



urlpatterns = [
    path('', views.getData),
    path('add/', views.addFolder),
    path('move_to_bin/<int:folder_id>/', move_to_bin, name='move_to_bin'),
    path('get_bin_data/', views.get_bin_data, name='get_bin_data'),


    

]