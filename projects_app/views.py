from dataclasses import fields
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project,Review,Tag
from django.views.generic import ListView,DetailView,TemplateView
from django.views.generic.edit import UpdateView,DeleteView,FormView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from users_app.search import SearchProject


from django import forms
# Create your views here.

def ProjList(request):
    proj_list,search_query=SearchProject(request)

    paginator1=Paginator(proj_list,3)
    page=request.GET.get('page')

    try:
        proj_list=paginator1.page(page)
    except PageNotAnInteger:
        page=1
        proj_list=paginator1.page(page)
    
    except EmptyPage:
        page=paginator1.num_pages
        proj_list=paginator1.page(page)


    return render(request,"projects.html",{'proj_list':proj_list,'search_query':search_query,'paginator1':paginator1})

"""class ProjDetail(UpdateView):
    model=Project
    context_object_name="proj"
    fields = "__all__"
    template_name="view.html"
    success_url =reverse_lazy('list1')"""


class ProjDelete(LoginRequiredMixin,DeleteView):
    model=Project
    context_object_name="proj"
    template_name="delete.html"
    success_url =reverse_lazy('myaccount1')
    login_url = reverse_lazy('login1')

# creating model form

class SupportToAdd(forms.ModelForm):
    class Meta:
        model=Project
        fields=["title","description","featured_image","demo_link","source_link",'tags']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }
    
    def __init__(self,*args,**kwargs):
        super(SupportToAdd,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})




@login_required(login_url="login1")
def ProjAdd(request,pk=0):

    if pk==0:

        if request.method=="POST":
            form=SupportToAdd(request.POST,request.FILES)

            if form.is_valid():
                newtags=request.POST.get('newtags').replace(',' , " ").split()

                project=form.save(commit=False)
                project.owner=request.user.profile
                project.save()
                for tag in newtags:
                    tagObj,created=Tag.objects.get_or_create(
                        name=tag,
                        )
                
                    project.tags.add(tagObj)
                messages.info(request,"Project Saved!")
                return redirect("myaccount1")
            else:
                form=SupportToAdd(request.FILES,request.POST)
                messages.warning(request,"Some error")
                return render(request,'form-template.html',{'form':form})

        else:

            form=SupportToAdd()
            return render(request,'form-template.html',{'form':form})
    else:

        if request.method=="POST":
            
            instance1=Project.objects.get(id=pk)
            form=SupportToAdd(request.POST,request.FILES,instance=instance1)

            if form.is_valid():

                newtags=request.POST.get('newtags').replace(',' , " ").split()
                project=form.save()
                for tag in newtags:
                    tagObj,created=Tag.objects.get_or_create(
                        name=tag,
                        )
                
                    project.tags.add(tagObj)

                messages.info(request,"Project Updated!")
                return redirect("myaccount1")
            else:
                instance1=Project.objects.get(id=pk)
                form=SupportToAdd(instance=instance1)
                messages.warning(request,"Some error occured!!")
                return render(request,'form-template.html',{'form':form,'project':instance1})
                


        else:
            instance1=Project.objects.get(id=pk)
            form=SupportToAdd(instance=instance1)
            return render(request,'form-template.html',{'form':form,'project':instance1})
        

class CommentSupprort(forms.ModelForm):
    class Meta:
        model=Review
        fields=['value','body']

        labels={
            'value':"Place your vote",
            'body': "Add a comment"
        }

    def __init__(self,*args,**kwargs):
        super(CommentSupprort,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


def ProjNo_Update(request,pk):
    project=Project.objects.get(id=pk)
    form=CommentSupprort()

    if request.method=="POST":
        form=CommentSupprort(request.POST)
        
        review=form.save(commit=False)
        review.owner=request.user.profile
        review.project=project
        review.save()
        project.getVoteCount
        messages.info(request,"Review added successfully!!!")
        return redirect('single1',pk=project.id)
           
        

    return render(request,'single-project.html',{'project':project,'form':form})
    







