# Generated by Django 4.2.1 on 2023-08-12 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_community', '0003_alter_teacher_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='license',
            field=models.ImageField(blank=True, null=True, upload_to='teacher_id_proofs/'),
        ),
    ]