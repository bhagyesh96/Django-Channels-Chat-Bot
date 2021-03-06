# Generated by Django 2.2.7 on 2020-08-20 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStatusModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('last_active', models.DateTimeField(auto_now=True, db_index=True, verbose_name='last_active')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_status', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
