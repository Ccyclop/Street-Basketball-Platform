from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('events/', views.EventsView.as_view()),
    path('events/<int:pk>', views.EventDetailView.as_view()),
    path('events/<int:pk>/comments', views.EventCreateComment.as_view()),
    path('comments/<int:pk>/', views.EventComments.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
