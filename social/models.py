from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    license = models.ImageField(upload_to='teacher_id_proofs/')

    # Set explicit related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='teachers'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='teachers'
    )

    def __str__(self):
        return self.username