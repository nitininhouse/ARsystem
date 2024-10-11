"""
URL configuration for autumn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from django.urls import path
from ars.views import (
    UserListCreateView, UserDetailView, UserRoleListCreateView, UserRoleDetailView, RoleListCreateView, RoleDetailView,
    TeamListCreateView, TeamDetailView, TeamAssignmentsView,
    AssignmentListCreateView, AssignmentDetailView, SubTaskListCreateView,
    SubTaskDetailView, AssignmentSubTasksView, SubmissionListCreateView,
    SubmissionDetailView, ResubmitView, ReviewListCreateView, ReviewDetailView,
    IterationReviewsView, CommentListCreateView, CommentDetailView,
    ProfileListCreateView, ProfileDetailView, ReviewHistoryView, SubmissionHistoryView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    

    path('userrole/', UserRoleListCreateView.as_view(), name='userrole-list-create'),
    path('userrole/<int:pk>/', UserRoleDetailView.as_view(), name='userrole-detail'),


    path('roles/', RoleListCreateView.as_view(), name='role-list-create'),
    path('roles/<int:pk>/', RoleDetailView.as_view(), name='role-detail'),
    
    path('teams/', TeamListCreateView.as_view(), name='team-list-create'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('teams/<int:pk>/assignments/', TeamAssignmentsView.as_view(), name='team-assignments'),
    
    path('assignments/', AssignmentListCreateView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentDetailView.as_view(), name='assignment-detail'),
    
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailView.as_view(), name='subtask-detail'),
    path('assignments/<int:pk>/subtasks/', AssignmentSubTasksView.as_view(), name='assignment-subtasks'),
    
    path('submissions/', SubmissionListCreateView.as_view(), name='submission-list-create'),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view(), name='submission-detail'),
    path('submissions/<int:pk>/resubmit/', ResubmitView.as_view(), name='resubmit-submission'),
    
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('assignments/<int:pk>/reviews/', IterationReviewsView.as_view(), name='iteration-reviews'),
    
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    
    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profiles/<int:pk>/review_history/', ReviewHistoryView.as_view(), name='review-history'),
    path('profiles/<int:pk>/submission_history/', SubmissionHistoryView.as_view(), name='submission-history'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



