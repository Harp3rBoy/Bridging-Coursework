from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import PersonalDetails
from .forms import DetailsForm


def home_page(request):
    try:
        details = get_object_or_404(PersonalDetails)
    except Http404:
        return render(request, 'cv/cv.html')
    return render(request, 'cv/cv.html', {'details': details})


def personal_details_edit(request):
    personal_details = PersonalDetails.objects.first()
    if request.method == "POST":
        form = DetailsForm(request.POST, instance=personal_details)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('home')
    else:
        form = DetailsForm(instance=personal_details)
    return render(request, 'cv/details_edit.html', {'form': form})
