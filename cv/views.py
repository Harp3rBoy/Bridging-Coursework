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


def details_edit(request):
    if request.method == "POST":
        form = DetailsForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('/cv')
    else:
        form = DetailsForm()
        return render(request, 'cv/details_edit.html', {'form': form})
