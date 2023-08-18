

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_user',
            field=models.ManyToManyField(blank=True, related_name='likes_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
