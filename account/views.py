from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from .forms import ProfileForm
from .models import Profile

# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "account/register.html", {
            "user_form": UserCreationForm,
            "profile_form": ProfileForm,
        })
    elif request.method == "POST":
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        try:
            user = user_form.save()
        except:
            return render(request, "account/register.html", {
                "user_form": user_form,
                "profile_form": profile_form,
            })
        profile = profile_form.save(commit=False)
        profile.user = user
        profile = profile_form.save()
        return HttpResponseRedirect(reverse("account:login"))

@login_required
def profile(request):
    return render(request, "account/profile.html", {
        "profile": Profile.objects.get(user=request.user)
    })
