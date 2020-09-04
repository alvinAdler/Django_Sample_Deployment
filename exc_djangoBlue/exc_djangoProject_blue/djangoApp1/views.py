from django.shortcuts import render
from djangoApp1.models import Tutor
from djangoApp1.forms import Basic_Form, Additional_Form

from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registrationPage(request):
    registered = False

    if request.method == "POST":
        basic_form = Basic_Form(data=request.POST)
        additional_form = Additional_Form(data=request.POST)

        if basic_form.is_valid() and additional_form.is_valid():
            basic = basic_form.save()
            basic.set_password(basic.password)
            basic.save()

            add = additional_form.save(commit=False)
            add.basic_user = basic
            if "basic_profpict" in request.FILES:
                add.basic_profpict = request.FILES["basic_profpict"]

            registered = True
            add.save()

            return HttpResponseRedirect(reverse("loginPage"))
        else:
            print(basic_form.errors, additional_form.errors)
    else:
        basic_form = Basic_Form()
        additional_form = Additional_Form()

    context_dict = {"registered":registered, "basic_form":basic_form, "additional_form":additional_form}
    return render(request, "djangoApp1/registrationPage.html", context=context_dict)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse("djangoApp1:mainPage"))
            else:
                return HttpResponse("Your account is not active!")
        else:
            return HttpResponse(f"Invalid login!\nInserted username: {username}\nInserted password: {password}")
    else:
        return render(request, "djangoApp1/loginPage.html", context={})

@login_required
def logoutPage(request):
    logout(request)
    return render(request, "djangoApp1/logoutPage.html", context={})

@login_required
def mainPage(request):
    return render(request, "djangoApp1/mainPage.html", context={})

@login_required
def tutorsPage(request):
    tutor_data = Tutor.objects.order_by("tutor_firstname")
    context_dict = {"tutor_data":tutor_data}
    return render(request, "djangoApp1/tutorsPage.html", context=context_dict)
