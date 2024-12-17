from django.urls import path
from . import views

urlpatterns = [
    path('stream/', views.stream_events, name='stream_events'),
    path('history/', views.event_history, name='event_history'),
]
