from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, null=True)
    resume = models.FileField(null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500, null=True)

    def register(self):
        self.save()

    def _str_(self):
        return self.user.username

    @staticmethod
    def get_student_by_email(email):
        return Student.objects.get(email=email)

class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, null=True)
    company = models.CharField(max_length=60)
    image = models.FileField(max_length=60,null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    company = models.CharField(max_length=60)
    type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=15, null=True)

    def _str_(self):
        return self.user.username

    def register(self):
        self.save()

    @staticmethod
    def get_recruiter_by_email(email):
        return Recruiter.objects.get(email=email)


class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=500, null=True)
    salary = models.FloatField(max_length=60)
    logo = models.FileField()
    description = models.CharField(max_length=300, null=True)
    experience = models.CharField(max_length=500)
    location = models.CharField(max_length=60)
    skills = models.CharField(max_length=15)
    creationdate = models.DateField()

    def _str_(self):
        return self.title

class Apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    resume = models.FileField(null=True)
    apply_date = models.DateField(null=True)


    def _str_(self):
        return self.id
