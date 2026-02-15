from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('check/', views.check_boyfriend, name='check'),
    path('wrong/', views.wrong_name, name='wrong'),
    path('story/', views.story, name='story'),
    path('story2/', views.story2, name="story2"),
    path('story3/', views.story3, name="story3"),
    path('story4/', views.story4, name="story4"),
    path('story5/', views.story5, name="story5"),
    path('story6/', views.story6, name="story6"),
    path('story7/', views.story7, name="story7"),
    path('story8/', views.story8, name="story8"),
    path('end/', views.end_story, name="end_story"),
    path('story9/', views.story9, name="story9"),
    path('story9-last/', views.story9_last, name='story9_last'),
    path('story10/', views.story10, name="story10"),
]