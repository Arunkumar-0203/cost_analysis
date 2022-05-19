from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib import messages
from django.views.generic import TemplateView

from tender.models import Guest, UserType, Senior, Contractor


class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "gust":
                    return redirect('/gust')
                elif UserType.objects.get(user_id=user.id).type == "senior":
                    return redirect('/senior')
                else:
                    return redirect('/contractor')
            else:
                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'login.html',{'message':"Invalid Username or Password"})




class GuestReg(TemplateView):
    template_name = 'gust_reg.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = Guest()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "gust"
             usertype.save()
             return redirect('gust_reg')
        except:
             messages = "Enter Another Username"
             return render(request,'gust_reg.html',{'messages':messages})


class SeniorReg(TemplateView):
    template_name = 'senior_reg.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = Senior()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "senior"
             usertype.save()
             return redirect('senior_reg')
        except:
             messages = "Enter Another Username"
             return render(request,'senior_reg.html',{'messages':messages})




class ContractorReg(TemplateView):
    template_name = 'contractor_reg.html'
    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        address = request.POST['address']
        contact = request.POST['contact']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
             user = User.objects.create_user(username=username,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = Contractor()
             reg.user = user
             reg.address = address
             reg.contact = contact
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "contractor"
             usertype.save()
             return redirect('contractor_reg')
        except:
             messages = "Enter Another Username"
             return render(request,'contractor_reg.html',{'messages':messages})