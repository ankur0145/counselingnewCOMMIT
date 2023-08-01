from django.urls import path
from .views import RegisterUserView, LoginUserView, LogoutUserView, UserDetailsView,QuestionListCreateView, TagListCreateView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('user/', UserDetailsView.as_view(), name='user-detail'),
    path('api/questions/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('api/tags/', TagListCreateView.as_view(), name='tag-list-create'),
    
]
