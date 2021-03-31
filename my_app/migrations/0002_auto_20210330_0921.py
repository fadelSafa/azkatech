# Generated by Django 3.1.7 on 2021-03-30 09:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeevacation',
            name='employee',
        ),
        migrations.AddField(
            model_name='employeevacation',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]