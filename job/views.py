from django.shortcuts import render, redirect
from job.models import *
from django.contrib.auth import authenticate, login 
from django.contrib.auth.hashers import check_password
from datetime import date

# Create your views here.


def index(request):
    return render(request, 'index.html')


def admin_login(request):
    if request.method == 'GET':
        return render(request, "admin_login.html")
    else:
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
    d = {'user': user}

    return render(request, "admin_home.html", d)



def user_login(request):
    if request.method == 'GET':
        return render(request, "user_login.html", )
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        student = Student.get_student_by_email(email)
        error_message = None
        if student:
            flage = check_password(password, student.password)
            if flage:
                return redirect("user_home")
            else:
                error_message = "Email or password invalid"
        else:
            error_message = "Email or password invalid"
        print(student)
        print(email, password)
        return render(request, "user_home.html", {'error': error_message})


def recruiter_login(request):
    if request.method == 'GET':
        return render(request, "recruiter_login.html", )
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        recruiter = Recruiter.get_recruiter_by_email(email)
        error_message = None
        if recruiter:
            flage = check_password(password, recruiter.password)
            if flage:
                return redirect("recruiter_home")
            else:
                error_message = "Email or password invalid"
        else:
            error_message = "Email or password invalid"
        print(recruiter)
        print(email, password)
        return render(request, "recruiter_home.html", {'error': error_message})


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    return render(request, 'user_home.html')


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    return render(request, 'recruiter_home.html', )



def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def Logout(request):
    request.session.clear()
    return redirect('index')

def user_signup(request):
    if request.method == 'GET':
        return render(request, 'user_signup.html')

    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        gender = postData.get('gender')
        resume = postData.get('resume')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, last_name, gender, resume, phone, email, password)
        student = Student(first_name=first_name,
                            last_name=last_name,
                            gender=gender,
                            resume=resume,
                            phone=phone,
                            email=email,
                            password=password)
        student.register()
        return render(request, 'user_login.html')


def recruiter_signup(request):
    if request.method == 'GET':
        return render(request, 'recruiter_signup.html')

    else:
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        gender = postData.get('gender')
        company = postData.get('company')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        print(first_name, last_name, gender, company, phone, email, password, type="recruiter", status="pending")
        recruiter = Recruiter(first_name=first_name,
                            last_name=last_name,
                            gender=gender,
                            company=company,
                            phone=phone,
                            email=email,
                            password=password)
        recruiter.register()
        return render(request, 'recruiter_login.html')

def view_users(request):
    data = Student.objects.all()
    d = {'data': data}
    return render(request, 'view_users.html', d)


def recruiter_pending(request):
    data = Recruiter.objects.filter(status="pending")
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)


def delete_user(request, pid):
    student = Student.objects.get(id=pid)
    student.delete()
    return redirect('view_users')


def delete_job(request, pid):
    job = User.objects.get(id=pid)
    job.delete()
    return redirect('job_list')

def change_status(request, pid):
    error = ""
    recruiter = Recruiter.objects.get(id=pid)
    if request.method == "POST":
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
        except:
            error = "yes"
    d = {'recruiter': recruiter, 'error': error}
    return render(request, 'change_status.html', d)


def recruiter_accepted(request):
    data = Recruiter.objects.filter(status="accepted")
    d = {'data': data}
    return render(request, 'recruiter_accepted.html', d)


def recruiter_rejected(request):
    data = Recruiter.objects.filter(status="rejected")
    d = {'data': data}
    return render(request, 'recruiter_rejected', d)


def all_recruiters(request):
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'all_recruiters', d)


def delete_recruiter(request,pid):
    recruiter = User.objects.get(id=pid)
    recruiter.delete()
    return redirect('recruiter_all')


def change_adminpassword(request):
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id.password)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_adminpassword.html', d)


def change_userpassword(request):
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id.password)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_userpassword', d)


def change_passwordrecruiter(request):
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id.password)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_passwordrecruiter.html', d)


def add_job(request):
    error = ""
    if request.method == "POST":
        start = request.POST['start_date']
        end = request.POST['end_date']
        t = request.POST['title']
        s = request.POST['salary']
        lo = request.POST['logo']
        des = request.POST['description']
        ex = request.POST['experience']
        loc = request.POST['location']
        ski = request.POST['skills']

        try:
            Job.objects.create(start_date=start, end_date=end, title=t, salary=s, logo=lo, description=des, experience=ex,  location=loc, skills=ski, creationdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_job.html', d)


def job_list(request):
    job = Job.objects.all()
    d = {'job': job}
    return render(request, 'job_list.html', d)


def edit_jobdetail(request, pid):
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == "POST":

        start = request.POST['start_date']
        end = request.POST['end_date']
        t = request.POST['title']
        s = request.POST['salary']
        c = request.POST['company']

        des = request.POST['description']
        ex = request.POST['experience']
        loc = request.POST['location']
        ski = request.POST['skills']

        job.title = t
        job.salary = s
        job.experience = ex
        job.locations = loc
        job.skills = ski
        job.description = des
        job.company = c
        try:
            job.save()
            error = "no"
        except:
            error = "yes"
        if start:
            try:
                job.start_date = start
                job.save()
            except:
                pass
        else:
            pass
        if end:
            try:
                job.end_date = end
                job.save()
            except:
                pass
        else:
            pass
    d = {'error': error, 'job': job}
    return render(request, 'edit_jobdetail.html', d)



def change_companylogo(request, pid):
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == "POST":

        cl = request.FILES['logo']
        job.logo = cl

        try:
            job.save()
            error = "no"
        except:
            error = "yes"

    d = {'error': error, 'job': job}
    return render(request, 'change_companylogo.html', d)


def latest_jobs(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job': job}
    return render(request, 'latest_jobs.html', d)


def user_latestjobs(request):
    job = Job.objects.all().order_by('-start_date')
    d = {'job': job}
    return render(request, 'user_latestjobs.html', d)


def job_detail(request, pid):
    job = Job.objects.get(id=pid)
    d = {'job': job}
    return render(request, 'job_detail.html', d)


def applyforjob(request, pid):
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == "POST":

        cl = request.FILES['logo']
        job.logo = cl

        try:
            job.save()
            error = "no"
        except:
            error = "yes"

    d = {'error': error, 'job': job}
    return render(request, 'applyforjob.html', d)


def applied_candidatelist(request):
    data = Student.objects.all()
    d = {'data': data}
    return render(request, 'applied_candidatelist.html', d)

