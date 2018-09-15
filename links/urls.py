from django.urls import path, re_path
from links import views



urlpatterns =[
	path('',views.LinkListView.as_view(), name = "home"),
]
