from django.urls import path
from . import views

#Add urls

urlpatterns=[
    path('about/',views.AboutView.as_view(),name='about')
]
