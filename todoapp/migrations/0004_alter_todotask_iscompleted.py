# Generated by Django 5.0.6 on 2024-06-04 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todotask_iscompleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='isCompleted',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]