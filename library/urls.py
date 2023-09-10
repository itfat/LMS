"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token

# from library.views import CustomLoginView
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include("user.urls")),
#     path('', include("book.urls"))
# ]


# urlpatterns += [
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Example login URL
#     # path('api-auth/', include('rest_framework.urls')),
#     # path('auth/login/', include('django.contrib.auth.urls')),
#     path('api-auth/login/', CustomLoginView.as_view(), name='custom_login'),
# ]



from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from library.views import UserView, signup



app_name = 'users'

urlpatterns = [
    path('users/', include('allauth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),
    path('profile/',  login_required(UserView.as_view()), name='profile'),
    path('signup/', signup, name='signup')
]


