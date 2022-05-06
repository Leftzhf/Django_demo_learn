from django.urls import path
from apps.users.views import UsernameCountView


urlpatterns =[
    path('usernames/<username>/count/',UsernameCountView.as_view())
]