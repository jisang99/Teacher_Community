from django.contrib import admin
<<<<<<< HEAD
# from .models import Funding
=======
>>>>>>> 1f0125c4c27d6047842480bf3d6da3948495111a

# Register your models here.
from .models import Teacher, Post, Comment, AttachedFile

admin.site.register(Teacher)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(AttachedFile)