from django.urls import path
from users.views import RegisterAPIView, UserDetailAPIView,UserStatusAPIView,UserLeaderAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view()),
    path('user/<int:pk>', UserDetailAPIView.as_view()),
    path('status/user/<int:pk>', UserStatusAPIView.as_view()),
    path('leader/user/<int:pk>', UserLeaderAPIView.as_view()),

]
