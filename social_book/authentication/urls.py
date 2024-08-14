# from django.urls import path
# from .views import login, signup, profile

# urlpatterns = [
#     path('login/', login, name='login'),
#     path('signup/', signup, name='signup'),
#     path('profile/', profile, name='profile'),

# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet, ProfileView, UserTypeView

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = [
    path('', include('djoser.urls')), 
    path('', include('djoser.urls.jwt')),  
    path('profile/', ProfileView.as_view(), name='profile'),
    path('users/type/<str:user_type>/', UserTypeView.as_view(), name='user_type'),
]
