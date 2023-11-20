from .models import Profile, Record
from .forms import RecordForm
from django.shortcuts import render, redirect

def dashboard(request):
    if request.method == "POST":
        form = RecordForm(request.POST or None)
        if form.is_valid():
            record = form.save(commit=False)
            record.user = request.user
            record.save()
            return redirect("dwitter:dashboard")
        
        followed_records = Record.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
        
    return render(request, "nilisoma/dashboard.html", {"form": form, "dweets": followed_records},)


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "nilisoma/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "nilisoma/profile.html", {"profile": profile})