from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from django.urls import path
from backened.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("contact/", ContactView.as_view(), name="contact"),
    path("register/", SignUpView.as_view(), name="register"),
    path("bio/", BioDataView.as_view(), name="bio"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginUser.as_view(), name="Login"),
]
