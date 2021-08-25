# Generated by Django 3.2.5 on 2021-07-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_auto_20210708_1259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
                ('company', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='resume',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]