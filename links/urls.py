from django.urls import path, re_path
from links import views
from django.contrib.auth.decorators import login_required as auth



urlpatterns =[
	path('',views.LinkListView.as_view(), name = "home"),
	path('signup/',views.SignUp.as_view(), name = "signup"),
	# path('profile/', views.ProfileListView.as_view(), name = 'profile'),
	path(r'^users/(?P<slug>\w+)/$', views.ProfileDetailView.as_view(), name="profile"),
	path(r'^edit_profile/(?P<slug>\w+)/$', auth(views.ProfileEditView.as_view()), name="edit_profile"),
	# path(r'^edit_profile/$', auth(views.ProfileEditView.as_view()), name="edit_profile"),
]