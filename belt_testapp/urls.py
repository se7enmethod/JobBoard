from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('create_job', views.create_job),
    path('process_job', views.process_job),
    path('edit/<int:job_id>', views.edit_job),
    path('edit_trip/<int:job_id>', views.process_edit_job),
    path('remove/<int:job_id>', views.remove_job),
    path('jobs/<int:job_id>', views.view_job),
    path('join/<int:job_id>', views.join_job),
    path('logout', views.logout),
]
