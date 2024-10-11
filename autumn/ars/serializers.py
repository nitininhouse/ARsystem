from rest_framework import serializers
from .models import User, Role, UserRole, Team, Assignment, SubTask, Submission, Review, Comment, Profile




# Custom User Serializer
class UserSerializer(serializers.ModelSerializer):
    roles = serializers.StringRelatedField(many=True)  # To display roles as strings, customize as needed

    class Meta:
        model = User  # Use your custom User model here
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'groups', 'user_permissions', 'roles']



# Role Serializer
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'role_name']


# UserRole Serializer

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = ['user', 'role']



# Team Serializer
class TeamSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()

    class Meta:
        model = Team
        fields = ['id', 'team_name', 'created_by']


# Assignment Serializer
class AssignmentSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    team = TeamSerializer()

    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'created_by', 'team']


# SubTask Serializer
class SubTaskSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer()

    class Meta:
        model = SubTask
        fields = ['id', 'title', 'description', 'assignment']


# Submission Serializer
class SubmissionSerializer(serializers.ModelSerializer):
    submitted_by = UserSerializer()
    assignment = AssignmentSerializer()

    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'submitted_by', 'status', 'comments', 'submission_date']


# Review Serializer
class ReviewSerializer(serializers.ModelSerializer):
    assignment = AssignmentSerializer()
    reviewer = UserSerializer()

    class Meta:
        model = Review
        fields = ['id', 'assignment', 'reviewer', 'iteration_number', 'comments', 'review_date']


# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    review = ReviewSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'review', 'created_by', 'comment_text', 'timestamp']


# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'review_history', 'submission_history', 'pending_reviews', 'in_progress_assignments']

