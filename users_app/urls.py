from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[

    path('login/',views.LoginPage,name="login1"),
    path('',views.LandingPage,name="profile1"),
    path('view/<str:pk>',views.CompleteProfile ,name="detail1"),
    path('logout/',views.LogoutPage,name="logout1"),
    path('register/',views.RegisterUser,name="register1"),
    path('forgot-pass/',views.ForgetPassword,name="forget100"),
    path('my-account/',views.UsersAccount,name="myaccount1"),
    path('edit-account/',views.EditAccount,name="editaccount1"),

    path("skill-add/",views.AddSkill,name="addskill1"),
    path("edit-skill/<str:pk>",views.AddSkill,name="editskill1"),
    path('delete-skill/<str:pk>',views.SkillDelete.as_view(),name="skilldelete1"),

    path('inbox/',views.Inbox,name="inbox1"),
    path("view-messages/<str:pk>",views.MessageView,name="messages1"),
    path('message-send-form/<str:pk>',views.SendMessage,name="sending1"),


    # The below views are builtin views. we need same name (url-name,name) as same below. otherwise it wont work.
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="forgetpassword.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="PasswordResetDone.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="PasswordResetConfirm.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="PasswordResetComplete.html"), name ='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)