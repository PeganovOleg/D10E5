from car.views import CarsView 
from django.urls import path  

app_name = 'car'  
urlpatterns = [  
    path('post', CarsView.as_view(), name='post-list'), 
    #path('i2/', CarsView, name='index'),  
    
   
]