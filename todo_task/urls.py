from django.urls import path
from . import views
urlpatterns =[
    # ADD TASK
    path('add_task/', views.add_task, name='add_task'),
    
    # Mark as done feature
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),

    # mark as undone feature
    path('mark_as_undone/<int:pk>/', views.mark_as_undone,name='mark_as_undone'),

    # Edit feature
    path('edit/<int:pk>/',views.edit, name='edit')
]