from .views import MemberLoginView, UserProfileView
from django.urls import path

urlpatterns = [
    path("login_user/", MemberLoginView.as_view(), name="login_user"),
    path("<str:username>/", UserProfileView.as_view(), name="user_profile"),
]
