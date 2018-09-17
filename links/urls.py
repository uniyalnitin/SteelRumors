from django.urls import path, re_path
from links import views
from django.contrib.auth.decorators import login_required as auth



urlpatterns =[
	path('',views.LinkListView.as_view(), name = "home"),
	path('signup/',views.SignUp.as_view(), name = "signup"),
	# path('profile/', views.ProfileListView.as_view(), name = 'profile'),
	path(r'^users/(?P<slug>\w+)/$', auth(views.ProfileDetailView.as_view()), name="profile"),
	path(r'^edit_profile/(?P<slug>\w+)/$', auth(views.ProfileEditView.as_view()), name="edit_profile"),
	# path(r'^edit_profile/$', auth(views.ProfileEditView.as_view()), name="edit_profile"),
	path(r'link/create/',auth(views.LinkCreateView.as_view()), name= "link_create"),
	path(r'^link/(?P<pk>\d+)/$', views.LinkDetailView.as_view(),name='link_detail'),
	path(r'^link/update/(?P<pk>\d+)/$', auth(views.LinkUpdateView.as_view()),name = "link_update"),
	path(r'^link/delete/(?P<pk>\d+)/$', auth(views.LinkDeleteView.as_view()),name = "link_delete"),
]