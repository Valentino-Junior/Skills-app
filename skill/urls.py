
from django.contrib import admin
from django.urls import path,include
from skillsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('skillsapp.urls')),
]
