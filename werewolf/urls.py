from django.contrib import admin
from django.urls import path, re_path #url
from .views import(
    were_wolf_detail_veiw,
    were_wolf_list_veiw,
    were_wolf_create_veiw,
    were_wolf_update_veiw,
    were_wolf_delete_veiw,
)



urlpatterns = [

     
    path('' ,were_wolf_list_veiw),
    path('<str:slug>/',were_wolf_detail_veiw),
    path('<str:slug>/edit/',were_wolf_update_veiw,'name=edit'),
    path('<str:slug>/delete/',were_wolf_delete_veiw),
    



] 
