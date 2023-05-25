from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update-room'),
    path('user-profile/<str:pk>/',views.uesrProfile,name='profile'),
    path('login-page/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('update-user/',views.updateUser,name='update-user'),
    path('signup/',views.registerUser,name='signup'),
    path('topics/',views.topics,name='topics'),
    path('activity/',views.activityPage,name='activity'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete-room'),
    path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message')
]


