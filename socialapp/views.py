from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView,TemplateView,View
from socialapp.forms import RegisterForm,LoginForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegisterForm

    def get_success_url(self):
        return reverse("sign_in")

    # def post(self,request,*args,**kwargs):
    #     form=RegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("sign_up")
    #     else:
    #         return render(request,"register.html",{"form":form})
    
class SingInView(FormView):
    template_name="login.html"
    form_class=LoginForm 

    def post(self,request,*args, **kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")  
            user_obj=authenticate(request,username=uname,password=pwd)
            if user_obj:
                login(request,user_obj)
                print(request.user)
                return redirect("index")
        print("invalid")
        return render(request,"login.html",{"form":form})
                
class IndexView(TemplateView):
    template_name="index.html"



class SignOutView(View):
    def get(self,request,*args, **kwargs):
        logout(request)
        return redirect("sign_in")  