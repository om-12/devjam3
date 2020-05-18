from django.urls import path

from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('FAQ',views.FAQ,name='FAQ'),
    path('rent',views.rent,name='rent'),
    path('rentyourhouse',views.rentyourhouse,name='rentyourhouse'),
    path('feedback',views.feedback,name='feedback'),
    path('showimage',views.showimage, name = 'showimage'), 
    path('success',views.success, name = 'success'), 
    path('rent',views.rent,name='rent'),
    path('rent2',views.rent2,name='rent2'),

    


]
