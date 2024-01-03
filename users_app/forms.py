from .models import Profile,Skill
from django import forms


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','username','location','short_intro','bio','profile_image','social_github','social_twitter','social_linkedin','social_youtube','social_website']

    def __init__(self,*args,**kwargs):
        super(ProfileEditForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class SkillSupport(forms.ModelForm):
    class Meta:
        model=Skill
        fields=["name","description"]
    
    def __init__(self,*args,**kwargs):
        super(SkillSupport,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})



    

        
        
