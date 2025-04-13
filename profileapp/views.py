from django.shortcuts import render
from django.views.generic import CreateView
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = "profile"
    form_class = ProfileCreationForm