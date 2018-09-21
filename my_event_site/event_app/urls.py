from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/new', views.list_new, name='list_new'),
    path('list/<int:pk_e>/<int:pk_l>', views.list_detail, name='list_detail'),
]