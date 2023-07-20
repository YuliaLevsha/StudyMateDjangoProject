from django.urls import path, re_path
from .views import *
from . import views


urlpatterns = [
    path('', main_page, name='home'),
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('addtopic/', addtopic_page, name='addtopic'),
    path('list_topic/', get_list_topic, name='list_topic'),
    path('list_topic/<uuid:topic_uuid>/', views.get_one_page, name='topic'),
    path('list_topic/<uuid:topic_uuid>/article/', views.add_article, name='article'),
    path('list_topic/<uuid:topic_uuid>/add_goal/', views.add_goal, name='add_goal'),
]

