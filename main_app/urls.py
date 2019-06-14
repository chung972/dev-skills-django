from django.urls import path
from . import views
# alternatively you could do something like this:
# from .views import *
# then in the urlpatterns, you would have:
#   path('', home, name="home"),

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_skill/', views.CreateSkill.as_view(), name="add_skill"),
    path('skills_index/', views.SkillsIndex.as_view(), name="skills_index"),
]