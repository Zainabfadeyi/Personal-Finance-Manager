# Generated by Django 5.0.1 on 2024-08-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='due_date',
        ),
        migrations.AlterField(
            model_name='saving',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(),
        ),
    ]
