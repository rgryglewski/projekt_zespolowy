from django.urls import path
from .views import Index, About, account

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("about", About.as_view(), name="about"),
    path("account", account, name="account"),
]
