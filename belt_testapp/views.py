from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Trip


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
        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
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
    my_trips = Trip.objects.filter(user=this_user)
    others_trips = Trip.objects.exclude(user=this_user)
    context = {
        "this_user": this_user,
        "my_trips": my_trips,
        "others_trips":others_trips
        }
    return render(request, 'dashboard.html', context)

def create_trip(request):
    return render(request, 'create_trip.html')

def process_trip(request):
    print(request.POST)
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/create_trip')
    destination = request.POST['destination']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']
    plan = request.POST['plan']
    context = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "plan": plan,
    }
    new_trip = Trip.objects.create(
        destination=request.POST['destination'], start_date=request.POST['start_date'], end_date=request.POST['end_date'], plan=request.POST['plan'])
    user_one = User.objects.get(id=request.session['user_id'])
    new_trip.user.add(user_one)
    return redirect('/dashboard', context)

def view_trip(request, trip_id):
    print(trip_id)
    this_trip=Trip.objects.get(id=trip_id)
    user_name=request.session['user_name']
    user_id = request.session['user_id']
    creator=User.objects.get(trips=trip_id)
    context = {
        'this_trip':this_trip,
        'user_id':user_id,
        'user_name':user_name,
        'creator':creator,
    }
    print(creator)
    return render(request, 'view_trip.html', context)

def join_trip(request, trip_id):
    pass


def edit_trip(request, trip_id):
    print(trip_id)
    trip_to_edit=Trip.objects.get(id=trip_id)
    destination = trip_to_edit.destination
    start_date = trip_to_edit.start_date
    end_date = trip_to_edit.end_date
    plan = trip_to_edit.plan
    context = {
        "destination": destination,
        "start_date": start_date,
        "end_date": end_date,
        "plan": plan,
        "trip_id":trip_id
    }
    print(end_date)
    return render(request, "edit_trip.html", context)

def process_edit_trip(request, trip_id):
    print(trip_id)
    x = trip_id
    errors = Trip.objects.trip_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/<int:trip_id>')
    trip_to_update=Trip.objects.get(id=trip_id)
    destination = trip_to_update.destination=request.POST['destination']
    start_date = trip_to_update.start_date=request.POST['start_date']
    end_date = trip_to_update.end_date=request.POST['end_date']
    plan = trip_to_update.plan=request.POST['plan']
    trip_to_update.save()
    context = {
        "trip_id" : trip_id,
        "destination": destination,
        "start_date":start_date,
        "end_date":end_date,
        "plan":plan
    }
    return redirect('/dashboard', context)

def remove_trip(request, trip_id):
    trip_to_remove=Trip.objects.get(id=trip_id)
    trip_to_remove.delete()
    return redirect('/dashboard')

def logout(request):
    print(request.session)
    request.session.flush()
    print(request.session)
    return redirect('/')
