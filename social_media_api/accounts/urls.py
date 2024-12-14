from django.urls import path
from .views import RegisterView, LoginView, UserProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile')
]
from django.urls import path
from .views import FollowViewSet

urlpatterns = [
    path('follow/<int:pk>/', FollowViewSet.as_view({'post': 'follow'}), name='follow'),
    path('unfollow/<int:pk>/', FollowViewSet.as_view({'post': 'unfollow'}), name='unfollow'),
]
