from .models import Profile
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


#@receiver(post_save,sender=P)  
def CreateProfile(sender,instance,created,**kwargs):
    print("Profile signal fired here!!!")
    if created:
        user=instance
        profile=Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user,

        )

        send_mail(
            "Hi There Welcome to devsearch",
            "We are glad you created account in devsearch!",
            "prathishgm14@gmail.com",
            [profile.email],
            fail_silently=False,
            )

def updateUser(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    if created==False:
        user.first_name=profile.name
        user.email=profile.email
        user.username=profile.username
        user.save()




def userDelete(sender,instance,**kwargs):


    try:
        user=instance.user

        if user.email:
            send_mail(
                "Your Account Deleted",
                "Account deleted successfully !!!",
                "prathishgm14@gmail.com",
                [user.email],
                fail_silently=False,
                )


        user.delete()
    
    except:
        pass


post_save.connect(CreateProfile,sender=User)

post_save.connect(updateUser,sender=Profile)

post_delete.connect(userDelete,sender=Profile)