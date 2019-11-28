from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('person', views.Person.as_view()),
    path('personDel', views.personDel.as_view()),

]