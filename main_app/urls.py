from django.urls import path
from . import views
# alternatively you could do something like this:
# from .views import *
# then in the urlpatterns, you would have:
#   path('', home, name="home"),

urlpatterns = [
    path('', views.home, name='home'),
]