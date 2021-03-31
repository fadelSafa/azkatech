from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from my_app.models import Vacation
from django.http import QueryDict, HttpResponse
from my_app.operations import  add_user_vacation, delete_user_vacation, update_user_vacation
# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request,'my_app/index.html')

def about(request):
    if request.method == 'GET':
        return render(request,'my_app/about.html')



@login_required(login_url='/') #redirect when user is not logged in
def dashboardView(request):
    return render(request,'registration/dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form':form})


#this method return the CRUD page empty without data
@login_required(login_url='/') #redirect when user is not logged in
def vacation(request):
    if request.method == "GET":
        return render(request,'registration/crud.html')  

#this method return the data in json format for specific user to fill them in CRUD page
@login_required(login_url='/') #redirect when user is not logged in
def get_vacation(request):
    if request.method == "GET":
       
       #getting all the vacation of the current user from the database
        object_list =Vacation.objects.filter(user=request.user.id)
        json = serializers.serialize('json', object_list)
        return HttpResponse(json, content_type='application/json')

# this method take the request to add vacation to specific user after Ajax validate it in front-end
# then validate the request in back-end also 
# save the record in database
# send the saved item in json format         
@login_required(login_url='/') #redirect when user is not logged in
def add_vacation(request):
    if request.method == "POST":
        status = add_user_vacation(request.user,request.POST.get("description"),request.POST.get("date_from"),request.POST.get("date_to"))
        return status
   


@login_required(login_url='/') #redirect when user is not logged in
def delete_vacation(request):

    if request.method == "DELETE":
        vacation_id = int(QueryDict(request.body).get('vacation_id'))
        status = delete_user_vacation(request.user,vacation_id)
        return status


@login_required(login_url='/') #redirect when user is not logged in
def update_vacation(request):
    if request.method == "PUT":
        put = QueryDict(request.body)
        status = update_user_vacation(request.user,put.get('id'),put.get('description'),put.get('date_from'),put.get('date_to'))
        return status
        