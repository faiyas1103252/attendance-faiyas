from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ("superadmin", "superadmin"),
        ("admin", "admin"),
        ("employee", "employee"),
    )

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
