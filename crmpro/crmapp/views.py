from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Record
def home(request):
    # Check to see if logging in
    records=Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('home')
        else:
            messages.error(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
        return render(request, 'crmapp/home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('home')

def about_us(request):
    return render(request, 'crmapp/about.html', {})

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'crmapp/register.html', {'form':form})

	return render(request, 'crmapp/register.html', {'form':form})


def customer_record(request,pk):
    if request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,'crmapp/record.html',{'customer_record':customer_record})
    else:
        messages.success(request,'You Must be logged in to view that record...')
        return redirect('home')

def delete_record(request,pk):
	if request.user.is_authenticated:
		record=Record.objects.get(id=pk)
		record.delete()
		messages.success(request,'The record has been deleted Successfully...')
		return redirect('home')
	else:
		messages.success(request,'You must be logged in to delete the records...')
		return redirect('home')

def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid:
                add_record=form.save()
                messages.success(request,'The has been added successfully!!!')
                return redirect('home')
            else:
                messages.success(request,'Please fill the correct form')
                return redirect('home')


        return render(request,'crmapp/add_record.html',{'form':form})

def update_record(request,pk):
    id=pk
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Form has been updated successfully!!!')
            return redirect('home')
        return render(request,'crmapp/update_record.html',{'form':form,'id':id})
    else:
        messages.success(request,'You have to be logged in to update the record!!!')
        return redirect('home')
