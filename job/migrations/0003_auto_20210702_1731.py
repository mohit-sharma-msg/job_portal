# Generated by Django 3.2.5 on 2021-07-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_student_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=15, null=True),
        ),
    ]