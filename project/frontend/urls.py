from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("submit", views.post),
    path("accounts/logout/", views.logout_view, name="logout"),
    path('accounts/profile/', views.profile, name="profile"),
    path("register", views.Register.as_view(), name="register")
]