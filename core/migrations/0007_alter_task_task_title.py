# Generated by Django 4.2.3 on 2023-08-01 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_task_create_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]