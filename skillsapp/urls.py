from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
 
re_path(r'^$',views.home,name='home'),

re_path(r'^search/', views.search_results,name='search_results')   ,
path('uploads',views.new_profile,name="upload_picture"),
path('select', views.query_skill, name='query_skill')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
