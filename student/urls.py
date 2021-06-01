from django.urls import path
from stud.views import stude_registration
urlpatterns=[
    path("studentreg",stude_registration,name="studreg")
]