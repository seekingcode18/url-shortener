from django.urls import path
from . import views

urlpatterns = [
    path('short/', views.UrlsListCreate.as_view()),
    path('auth/<str:pk>/', views.url_auth_redirect),
    path('<str:pk>/', views.url_redirect),
    path('api/urls/', views.UrlsListCreate.as_view()),
    path('api/urls_auth/', views.UrlsListCreateAuth.as_view()),
    path('^api/urls/user/(?P<username>.+)/$', views.UsersUrlsList.as_view()),
    path('api/urls/<int:pk>', views.UrlsDelete.as_view()),
    path('api/urls_auth/<int:pk>', views.UrlsDeleteAuth.as_view())
]