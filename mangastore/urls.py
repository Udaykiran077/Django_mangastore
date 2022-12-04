from django.urls import path
from . import views

urlpatterns = [path("",views.index , name = "index"),
path("uk.html",views.uk , name= "uk"),
path("register.html",views.register , name = "register" )
]

