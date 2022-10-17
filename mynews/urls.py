from django.urls import path
from . import views


urlpatterns = [
 path("home/",views.home,name="home"),
 path("politics",views.politics,name="politics"),
 path("sports",views.sports,name="sports"),
 path("education",views.education,name="education"),
 path("travel",views.travel,name="travel"),
 path("health",views.health,name="health"),
] 