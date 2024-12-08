from django.urls import path  
from . import views  

urlpatterns = [  
    path('', views.PostListView.as_view(), name='post-list'),  
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),  
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'),  
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  
    path('register/', views.register, name='register'),  
    path('login/', views.LoginView.as_view(), name='login'),  
    path('logout/', views.LogoutView.as_view(), name='logout'),  
    path('profile/', views.profile, name='profile'),  
]  
