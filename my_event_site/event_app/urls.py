from django.urls import path
from . import views

urlpatterns = [
	# landing page
    path('', views.event_list, name='event_list'),

    # events
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/new', views.event_new, name='event_new'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),

    #lists
    path('list/<int:pk>/new', views.list_new, name='list_new'),
    path('list/<int:pk>/<int:pk2>', views.list_detail, name='list_detail'),
    path('list/<int:pk>/<int:pk2>/edit/', views.list_edit, name='list_edit'),

    # guestlists
    path('guestlist/<int:pk>/', views.guestlist_detail, name='guestlist_detail'),
    path('guestlist/<int:pk>/', views.guestlist_detail, name='guestlist_detail'),

    # items
    path('item/<int:pk>/<int:pk2>', views.item_new, name='item_new'),
    path('item/<int:pk>/<int:pk2>/<int:pk3>/edit/', views.item_edit, name='item_edit'),

    #persons
    path('person/<int:pk>/', views.person_new, name='person_new'),
]