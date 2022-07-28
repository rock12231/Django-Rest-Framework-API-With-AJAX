from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from baseAPI import views

urlpatterns = [
    path('emp/', views.EmpList.as_view()),
    path('emp/<int:pk>/', views.EmpDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)