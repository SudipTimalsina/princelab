# student/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Create
    path('create/', views.student_create_view, name='student-create'),

    # Read
    path('list/', views.student_list_view, name='student-list'),
    path('detail/<int:id>/', views.student_detail_view, name='student-detail'),

    # Update
    path('update/<int:id>/', views.student_update_view, name='student-update'),

    # Delete
    path('delete/<int:id>/', views.student_delete_view, name='student-delete'),
]
