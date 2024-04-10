from django.db import models
from django.contrib.auth.models import User

class Internship(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # Teacher who posted the internship
    is_active = models.BooleanField(default=True)
    
    class Meta:
        permissions = [
            ("can_post_internship", "Can post internship"),
            ("can_edit_internship", "Can edit internships"),
            ("can_delete_internship", "Can delete internships"),
            ("can_apply_to_internship", "Can apply to internships"),
            ("can_view_applied_internships", "Can view all applied internships"),
            ("can_view_internship_applications", "Can view all applications to internships"),
        ]
    def __str__(self):
        return self.title

class Application(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Student who applied for the internship
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('internship', 'student')  # Ensure a student can apply to an internship only once

    def __str__(self):
        return f"{self.student.username} applied for {self.internship.title}"
