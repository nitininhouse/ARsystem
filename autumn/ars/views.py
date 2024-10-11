from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, UserRole , Role, Team, Assignment, SubTask, Submission, Review, Comment, Profile
from .serializers import (
    UserSerializer, UserRoleSerializer , RoleSerializer, TeamSerializer, AssignmentSerializer,
    SubTaskSerializer, SubmissionSerializer, ReviewSerializer, CommentSerializer, ProfileSerializer
)
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



# CBV for User
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

    

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserRoleListCreateView(generics.ListCreateAPIView):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    permission_classes = [AllowAny]
      # Only authenticated users can access

# Detail View for UserRole (Retrieve, Update, Delete)
class UserRoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserRole.objects.all()  # Change to UserRole queryset
    serializer_class = UserRoleSerializer
    permission_classes = [AllowAny]
    

# CBV for Role
class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

# CBV for Team
class TeamListCreateView(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

class TeamAssignmentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        team = get_object_or_404(Team, pk=pk)
        assignments = Assignment.objects.filter(team=team)
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)

# CBV for Assignment
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

class AssignmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]

# CBV for SubTask
class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]

class SubTaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    permission_classes = [IsAuthenticated]

class AssignmentSubTasksView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        assignment = get_object_or_404(Assignment, pk=pk)
        subtasks = SubTask.objects.filter(assignment=assignment)
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)

# CBV for Submission
class SubmissionListCreateView(generics.ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

class SubmissionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

class ResubmitView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk, format=None):
        submission = get_object_or_404(Submission, pk=pk)
        submission.status = 'resubmitted'
        submission.save()
        return Response({"status": "resubmitted"}, status=status.HTTP_200_OK)

# CBV for Review
class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]

class IterationReviewsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        assignment = get_object_or_404(Assignment, pk=pk)
        reviews = Review.objects.filter(assignment=assignment).order_by('iteration_number')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

# CBV for Comment
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

# CBV for Profile
class ProfileListCreateView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ReviewHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        profile = get_object_or_404(Profile, pk=pk)
        return Response({"review_history": profile.review_history})

class SubmissionHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        profile = get_object_or_404(Profile, pk=pk)
        return Response({"submission_history": profile.submission_history})

# Create your views here.
