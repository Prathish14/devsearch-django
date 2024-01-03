from .models import Profile,Skill
from projects_app.models import Project,Tag
from django.db.models import Q


def SearchDeveloper(request):

    search_query1=""
    if request.GET.get("search_query"):
        search_query1=request.GET.get('search_query')

    skills=Skill.objects.filter(name__icontains=search_query1)

    profiles=Profile.objects.distinct().filter(Q(name__icontains=search_query1)|Q(short_intro__icontains=search_query1)|Q(skill__in=skills))



    return profiles,search_query1

def SearchProject(request):
    search_query=""
    if request.GET.get('search_project'):
        search_query=request.GET.get('search_project')

    tag=Tag.objects.filter(name__icontains=search_query)
    owner=Profile.objects.filter(name__icontains=search_query)

    proj_list=Project.objects.distinct().filter(Q(title__icontains=search_query)|Q(description__icontains=search_query)|Q(tags__in=tag)|Q(owner__name__icontains=search_query))
    return proj_list,search_query



