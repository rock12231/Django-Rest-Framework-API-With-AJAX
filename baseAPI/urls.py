from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from baseAPI import views

urlpatterns = [
    path('', views.SnippetPage.as_view()),
    path('api/snippet/', views.SnippetList.as_view()),
    path('api/snippet/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)