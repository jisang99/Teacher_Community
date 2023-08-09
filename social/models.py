from django.db import models
# Create your models here.
class Teacher(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    license = models.ImageField(upload_to='teacher_id_proofs/')

    def __str__(self):
        return self.username
    

