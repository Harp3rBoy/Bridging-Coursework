from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import PersonalDetails, Education
from .forms import PersonalDetailsForm, EducationForm


def home_page(request):
    try:
        details = get_object_or_404(PersonalDetails)
    except Http404:
        return render(request, 'cv/cv.html')
    return render(request, 'cv/cv.html', {'details': details})


def personal_details_edit(request):
    personal_details = PersonalDetails.objects.first()
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST, instance=personal_details)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = PersonalDetailsForm(instance=personal_details)
    return render(request, 'cv/details_edit.html', {'form': form})


def education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = EducationForm()
    return render(request, 'cv/details_edit.html', {'form': form})
