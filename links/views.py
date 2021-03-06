from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView, UpdateView, DeleteView


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import get_user_model
from .models import Link, Vote, Profile
from .forms import LinkForm

# Create your views here.

class LinkListView(ListView):
	model =Link
	queryset = Link.with_votes.all()
	paginate_by =3

class LinkCreateView(CreateView):
	model =Link
	form_class = LinkForm

	def form_valid(self,form):
		f = form.save(commit=False) #calling the form, but we dont want to commit yet.
		f.rank_score=0.0
		f.submitter = self.request.user
		f.save()
		return super(LinkCreateView,self).form_valid(form)

class LinkDetailView(DetailView):
	model = Link

class LinkUpdateView(UpdateView):
	model = Link
	form_class = LinkForm

class LinkDeleteView(DeleteView):
	model = Link
	success_url = reverse_lazy("home")

class SignUp(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'registration/signup.html'

class ProfileDetailView(DetailView):
	model = get_user_model()
	slug_field = "username"
	template_name ="registration/user_detail.html"

	def get_object(self,queryset=None):
		user = super(ProfileDetailView,self).get_object(queryset)
		Profile.objects.get_or_create(user = user)
		return user

class ProfileEditView(UpdateView):
	model = Profile
	template_name= "registration/edit_profile.html"
	slug_field="username"
	fields = ['bio','location','birth_date']
	# form_class = ProfileForm
	# user = Profile.objects.get(user=self.request.user)[0]
	# user.profile.bio = request.POST['bio']
	def get_object(self,queryset=None):
		user = self.request.user
		return user.profile

	# def form_valid(self, form):
	# 	self.object = form.save()
	# 	return super().form_valid(form)

	def get_success_url(self):
		return reverse("profile", kwargs={'slug':self.request.user})