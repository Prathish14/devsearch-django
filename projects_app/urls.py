from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    #path('index/',views.Index_Page.as_view(),name="index1"),
    path('',views.ProjList,name="projects1"),
    #path('',views.Index_Page.as_view(),name="projects1"),

    path('single-project/<str:pk>',views.ProjNo_Update,name="single1"),
    path('add/',views.ProjAdd,name="add1"),

    path('project/<str:pk>',views.ProjAdd,name="editproject1"),

    
    
    #path('view/<str:pk>',views.ProjDetail.as_view(),name="pdetail"),
    path('delete/<str:pk>',views.ProjDelete.as_view(),name="delete1"),
    
    #path('view/<str:pk>',views.view,name="view1"),
]

#Guiding Media URL to look MEDIA ROOT for the images while site is running
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)