from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
   
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='ars_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='ars_users_permissions',
        blank=True
    )
    roles = models.ManyToManyField('Role', related_name='users', blank=True)

    def __str__(self):
        return self.username


class Role(models.Model):
    
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('reviewer', 'Reviewer'),
        ('reviewee', 'Reviewee'),
    )
    role_name = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.role_name


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role.role_name}"
    
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teams_created")

    def __str__(self):
        return self.team_name

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignments_created')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class SubTask(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='subtasks')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Submission(models.Model):
    SUBMISSION_STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('submitted', 'Submitted'),
        ('resubmitted', 'Resubmitted'),
    )

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    status = models.CharField(max_length=20, choices=SUBMISSION_STATUS_CHOICES)
    comments = models.TextField(blank=True, null=True)
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Submission by {self.submitted_by.username} for {self.assignment.title}"

class Review(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_done')
    iteration_number = models.PositiveIntegerField(default=1)
    comments = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.iteration_number} of {self.assignment.title} by {self.reviewer.username}"


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_comments')  
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.created_by.username} on {self.review}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    review_history = models.TextField(blank=True, null=True)  
    submission_history = models.TextField(blank=True, null=True)  
    pending_reviews = models.PositiveIntegerField(default=0)
    in_progress_assignments = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Profile of {self.user.username}"

