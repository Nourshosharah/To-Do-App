from django.urls import path 
from .views import *
from . import views
urlpatterns=[
    path("",index, name='index'),
    path("all/",all,name='all'),
    path('delete_item/<int:item_id>/',delete_item, name="delete_item"),
    path('edit/<int:id_item>',edit_item,name='edit'),
    path('update_item/<int:id_item>', views.update_item,name='update')
  
    
]