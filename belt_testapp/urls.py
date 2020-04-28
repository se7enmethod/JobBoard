from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('dashboard', views.dashboard),
    path('create_trip', views.create_trip),
    path('process_trip', views.process_trip),
    path('edit/<int:trip_id>', views.edit_trip),
    path('edit_trip/<int:trip_id>', views.process_edit_trip),
    path('remove/<int:trip_id>', views.remove_trip),
    path('trips/<int:trip_id>', views.view_trip),
    path('join/<int:trip_id>', views.join_trip),
    path('logout', views.logout),
]
