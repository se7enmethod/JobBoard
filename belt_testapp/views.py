from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Job


def index(request):
    return render(request, 'index.html')


def register(request):
    print(request.POST)
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print('there was an error, try again')
        return redirect('/')
    else:
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
        request.session['user_id'] = new_user.id
        request.session['user_name'] = new_user.first_name
        print('created user redirect to dashboard')
    return redirect('/dashboard')


def login(request):
    print(request.session)
    login_user = User.objects.filter(email=request.POST['email'])
    if len(login_user) > 0:
        login_user = login_user[0]
        if login_user.password == request.POST['password']:
            request.session['user_id'] = login_user.id
            request.session['user_name'] = login_user.first_name
            return redirect('/dashboard')
        print('Incorrect Password')
    print('Logged in')
    return redirect('/')


def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = request.session['user_id']
    my_jobs = Job.objects.filter(user=this_user)
    others_jobs = Job.objects.exclude(user=this_user)
    context = {
        "this_user": this_user,
        "my_job": my_jobs,
        "others_jobs":others_jobs
        }
    return render(request, 'dashboard.html', context)

def create_job(request):
    return render(request, 'create_job.html')

def process_job(request):
    print(request.POST)
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create_job')
    job_title = request.POST['job_title']
    category = request.POST['category']
    location = request.POST['location']
    description = request.POST['description']
    context = {
        "job_title": job_title,
        "category": category,
        "location": location,
        "description": description,
    }
    new_job = Job.objects.create(
        job_title=request.POST['job_title'], category=request.POST['category'], location=request.POST['location'], description=request.POST['description'])
    user_one = User.objects.get(id=request.session['user_id'])
    new_job.user.add(user_one)
    return redirect('/dashboard', context)

def view_job(request, job_id):
    print(job_id)
    this_job=Job.objects.get(id=job_id)
    user_name=request.session['user_name']
    user_id = request.session['user_id']
    creator=User.objects.get(jobs=job_id)
    context = {
        'this_job':this_job,
        'user_id':user_id,
        'user_name':user_name,
        'creator':creator,
    }
    print(creator)
    return render(request, 'view_job.html', context)

def join_job(request, job_id):
    pass


def edit_job(request, job_id):
    print(job_id)
    job_to_edit=Job.objects.get(id=job_id)
    destination = job_to_edit.destination
    start_date = job_to_edit.start_date
    end_date = job_to_edit.end_date
    plan = job_to_edit.plan
    context = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "plan": plan,
        "job_id":job_id
    }
    print(end_date)
    return render(request, "edit_job.html", context)

def process_edit_job(request, job_id):
    print(job_id)
    x = job_id
    errors = Job.objects.job_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/<int:job_id>')
    job_to_update=Job.objects.get(id=job_id)
    destination = job_to_update.destination=request.POST['destination']
    start_date = job_to_update.start_date=request.POST['start_date']
    end_date = job_to_update.end_date=request.POST['end_date']
    plan = job_to_update.plan=request.POST['plan']
    job_to_update.save()
    context = {
        "job_id" : job_id,
        "destination": destination,
        "start_date":start_date,
        "end_date":end_date,
        "plan":plan
    }
    return redirect('/dashboard', context)

def remove_job(request, job_id):
    job_to_remove=Job.objects.get(id=job_id)
    job_to_remove.delete()
    return redirect('/dashboard')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')
