from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('list/<int:pk>/new', views.list_new, name='list_new'),
    path('list/<int:pk>/<int:pk2>', views.list_detail, name='list_detail'),
    path('list/<int:pk>/<int:pk2>/edit/', views.list_edit, name='list_edit'),
    path('guestlist/<int:pk>/', views.guestlist_detail, name='guestlist_detail'),
    path('guestlist/<int:pk>/', views.guestlist_detail, name='guestlist_detail'),
    path('item/<int:pk>/<int:pk2>', views.item_new, name='item_new'),
    path('item/<int:pk>/<int:pk2>/<int:pk3>/edit/', views.item_edit, name='item_edit'),
    path('person/<int:pk>/', views.person_new, name='person_new'),
]