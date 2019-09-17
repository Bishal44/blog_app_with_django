from account.api.views import (
registration_view,
)
from django.urls import path
app_name = "Account"
urlpatterns = [

    path('register', registration_view, name="registration"),
    ]