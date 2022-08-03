from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.TeamListView.as_view()),
    path('<int:pk>', views.TeamDetailView.as_view()),
    path('<int:pk>/players', views.TeamMembersView.as_view()),
    path('players/<int:pk>', views.PlayerDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) 