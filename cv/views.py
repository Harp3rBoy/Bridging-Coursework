from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404
from .models import PersonalDetails, Education, WorkExperience
from .forms import PersonalDetailsForm, EducationForm, WorkExperienceForm


def home_page(request):
    personal_details = PersonalDetails.objects.first()
    education = Education.objects.all()
    work_experience = WorkExperience.objects.all()
    return render(request, 'cv/cv.html', {'personal_details': personal_details, 'education': education,
                                          'work_experience': work_experience})


@login_required
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


@login_required
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


@login_required
def education_edit(request, pk):
    post = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = EducationForm(instance=post)
    return render(request, 'cv/details_edit.html', {'form': form, 'name': 'Edit Education'})


@login_required
def education_remove(request, pk):
    post = get_object_or_404(Education, pk=pk)
    post.delete()
    return redirect('home')


@login_required
def work_experience_new(request):
    if request.method == "POST":
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = WorkExperienceForm()
    return render(request, 'cv/details_edit.html', {'form': form, 'name': 'New Work Experience'})


@login_required
def work_experience_edit(request, pk):
    post = get_object_or_404(WorkExperience, pk=pk)
    if request.method == "POST":
        form = WorkExperienceForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = WorkExperienceForm(instance=post)
    return render(request, 'cv/details_edit.html', {'form': form, 'name': 'Edit Work Experience'})


@login_required
def work_experience_remove(request, pk):
    post = get_object_or_404(WorkExperience, pk=pk)
    post.delete()
    return redirect('home')
