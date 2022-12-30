from rest_framework import routers
from django.urls import path
from users.api import (
    UserViewSet, UserViewSetOne, LoginView, SignUpView, GetUser)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

router = routers.DefaultRouter()

# router.register('/v1/users', UserViewSet, 'users')
# router.register('/v1/oneusers', UserViewSetOne, 'oneUser')
router.register('/get', GetUser)

urlpatterns = [
    path('/signup/', SignUpView.as_view(), name= 'signup'),
    path('/login/', LoginView.as_view(), name= 'login'),
    path('/jwt_create', TokenObtainPairView.as_view(), name= 'jwt_create'),
    path('/jwt_refresh', TokenRefreshView.as_view(), name= 'token_refresh'),
    path('/jwt_verify', TokenVerifyView.as_view(), name= 'token_verify'),
]


urlpatterns += router.urls