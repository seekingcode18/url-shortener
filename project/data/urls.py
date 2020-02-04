from django.urls import path
from . import views

urlpatterns = [
    path('short/', views.UrlsListCreate.as_view()),
    path('<str:pk>', views.url_redirect),
    path('api/urls/', views.UrlsListCreate.as_view()),
    path('api/urls/<int:pk>', views.UrlsDelete.as_view())
]