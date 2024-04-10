from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    
    path('internship/post', views.post_internship, name='post_internship'),
    path('internship/edit/<int:internship_id>/', views.edit_internship, name='edit_internship'),
    path('internship/delete/<int:internship_id>/', views.delete_internship, name='delete_internship'),
    path('internship/apply/<int:internship_id>/', views.apply_internship, name='apply_internship'),
    path('internship/applied/', views.applied_internships, name='applied_internships'),
    path('internship/applications/<int:internship_id>/', views.internship_applications, name='internship_applications')
]
