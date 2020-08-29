from django.shortcuts import redirect, render
from .models import PersonalDetails, Education
from .forms import PersonalDetailsForm, EducationForm


def home_page(request):
    personal_details = PersonalDetails.objects.first()
    education = Education.objects.all()
    return render(request, 'cv/cv.html', {'personal_details': personal_details, 'education': education})


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
    return render(request, 'cv/details_edit.html', {'form': form, 'name': 'Edit Personal Details'})


def education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = EducationForm()
    return render(request, 'cv/details_edit.html', {'form': form, 'name': 'New Education'})
