from django.urls import path
from . import views

urlpatterns = [
    #Profile Page
    path('', views.profile_view, name='profile_view'),
    
    #Generic Registeration Page
    path('register/', views.register_view, name='register_common'),
    
    #Called on basis of what is selected above
    path('register/student/', views.register_student, name='register_student'),
    path('register/teacher/', views.register_teacher, name='register_teacher'),
    
    #Generic Login/Logout Page
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    
    #Generic Edit if needed
    path('edit/', views.edit_profile_view, name='edit_profile_view')
]
