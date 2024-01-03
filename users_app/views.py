from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Profile,Skill,Message

from django import forms

from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileEditForm,SkillSupport

from django.views.generic.edit import UpdateView,DeleteView,FormView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

#for searching (enhanced search functionality)
from django.db.models import Q
from .search import SearchDeveloper

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def LandingPage(request):

    profiles,search_query1=SearchDeveloper(request)
    paginator1=Paginator(profiles,3)

    try:
        page1=request.GET.get("page")
        profiles=paginator1.page(page1)
    except PageNotAnInteger:
        page1=1
        profiles=paginator1.page(page1)
    except EmptyPage:
        page1=paginator1.num_pages
        profiles=paginator1.page(page1)

    return render(request,"index1.html",{'profiles':profiles,'search_query1':search_query1,'paginator1':paginator1})
    
    

        
    

def CompleteProfile(request,pk):
   profile=Profile.objects.get(id=pk)
   topskills=profile.skill_set.exclude(description__exact="")
   otherskills=profile.skill_set.filter(description="")
   return render(request,'profile.html',{'profile':profile,'topskills':topskills,'otherskills':otherskills})


def LoginPage(request):
    

    if request.user.is_authenticated:
        return redirect('profile1')
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request, "Username is Not correct.")

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"You have successfully logged in")
            return redirect(request.GET['next'] if 'next' in request.GET else 'myaccount1' )
        else:
            messages.error(request, "Username/Password is Not correct.")

            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
@login_required(login_url="login1")   
def LogoutPage(request):
    messages.warning(request, "User Logged out.")
    logout(request)
    return redirect('login1')


class CustomRegistration(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]
        labels={
            'first_name':"Name"
        }
    
    def __init__(self,*args,**kwargs):
        super(CustomRegistration,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



def RegisterUser(request):

    if request.method=="POST":

        form=CustomRegistration(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()

            messages.success(request,"User Registration Successfull")

            login(request,user)
            return redirect("editaccount1")
        else:
            messages.error(request,"An error occured during registration")
            form=CustomRegistration(request.POST)
            return render(request,'signup.html',{'form':form})
    else:

        form=CustomRegistration
        return render(request,'signup.html',{'form':form})
    

def ForgetPassword(request):
    return render(request,'forgetpassword.html')


@login_required(login_url="login1")
def UsersAccount(request):
    profile=request.user.profile
    return render(request,"account.html",{'profile':profile})

@login_required(login_url="login1")
def EditAccount(request):

    if request.method=="POST":
        form=ProfileEditForm(request.POST,request.FILES,instance=request.user.profile)

        if form.is_valid():
            form.save()
            messages.info(request,"Profile Updated Successfully!")
            return redirect('myaccount1')
        else:
            messages.error(request,"Error in your submission")
            form=ProfileEditForm(request.POST,request.FILES,instance=request.user.profile)
            return render(request,"edit_account.html",{'form':form})

    
    else:
        form=ProfileEditForm(instance=request.user.profile)
        return render(request,"edit_account.html",{'form':form})
    
@login_required(login_url="login1")
def AddSkill(request,pk=0):

    if pk==0:

        if request.method=="POST":
            form=SkillSupport(request.POST)

            if form.is_valid():
                person=form.save(commit=False)
                person.owner=request.user.profile
                person.save()
                messages.success(request,"Skill Added Successfully!!!")
                return redirect("myaccount1")
            else:
                form=SkillSupport(request.POST)
                messages.error(request,"Error occured while adding skills!")
                return render(request,"skill.html",{'form':form})

            
        else:

            form=SkillSupport()
            return render(request,"skill.html",{'form':form})
    
    else:

        if request.method=="POST":
            instance1=Skill.objects.get(id=pk)
            form=SkillSupport(request.POST,instance=instance1)

            if form.is_valid():
                form.save()
                messages.success(request,"Skill Updated Successfully!!!")
                return redirect("myaccount1")
            else:
                instance1=Skill.objects.get(id=pk)
                form=SkillSupport(request.POST,instance=instance1)
                messages.error(request,"Some error occured!!!")
                return render(request,"skill.html",{'form':form})





        else:
            instance1=Skill.objects.get(id=pk)
            form=SkillSupport(instance=instance1)
            return render(request,"skill.html",{'form':form})
        


class SkillDelete(LoginRequiredMixin,DeleteView):
    model=Skill
    context_object_name="skill"
    template_name="skill-delete.html"
    success_url =reverse_lazy('myaccount1')
    login_url = reverse_lazy('login1')


def Inbox(request):

    profile=request.user.profile
    message_request=profile.messages.all()
    UnReadCount=message_request.filter(is_read=False).count()
    context={'message_request':message_request,'UnReadCount':UnReadCount}
    return render(request,"inbox.html",context)

def MessageView(request,pk):

    message_view=Message.objects.get(id=pk)

    if message_view.is_read == False:
        message_view.is_read=True
        message_view.save()

    context={'message_view':message_view}

    return render(request,"message.html",context)

class SendMessageSupport(forms.ModelForm):
    class Meta:
        model=Message
        fields=['name','email','subject','body']

    def __init__(self,*args,**kwargs):
        super(SendMessageSupport,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

def SendMessage(request,pk):

    if request.method=="POST":

        if request.user.is_authenticated:

            reciver=Profile.objects.get(id=pk)


            form=SendMessageSupport(request.POST)

            if form.is_valid():
                message1=form.save(commit=False)
                message1.sender=request.user.profile
                message1.recipient=reciver
                message1.name=request.user.profile.name
                message1.email=request.user.profile.email
                message1.save()
                messages.success(request,"Message sent successfully!!!")
                return redirect('detail1',pk=pk)
            else:
                messages.error(request,"Some Unknown error occured!!!")
                return redirect('detail1',pk=pk)
            
        else:
            form=SendMessageSupport(request.POST)
            reciver=Profile.objects.get(id=pk)

            if form.is_valid():
                message1=form.save(commit=False)
                message1.recipient=reciver
                message1.sender=None
                message1.save()
                messages.success(request,"Message sent successfully!!!")
                return redirect('detail1',pk=pk)
            else:
                messages.error(request,"Some Unknown error occured!!!")
                return redirect('detail1',pk=pk)



    else:

        form=SendMessageSupport()
            
        return render(request,"form-message.html",{'form':form})
    
        




