from django.contrib import admin
from django.urls import path, include
from users.rest_views import GoogleLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),
]
