# Generated by Django 4.0.3 on 2022-03-20 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0005_remove_admin_admin_remove_admin_superadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='profpic',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]