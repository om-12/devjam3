from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ 
    path('showimage',views.showimage, name = 'showimage'), 
     
] 
  
