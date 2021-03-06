# Generated by Django 3.2.5 on 2021-08-02 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0013_auto_20210731_0808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=500, null=True)),
                ('salary', models.FloatField(max_length=60)),
                ('image', models.FileField(upload_to='')),
                ('discription', models.CharField(max_length=300, null=True)),
                ('experience', models.CharField(max_length=500)),
                ('location', models.CharField(max_length=60)),
                ('skills', models.CharField(max_length=15)),
                ('creationdate', models.DateField()),
                ('recruiter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job.recruiter')),
            ],
        ),
    ]
