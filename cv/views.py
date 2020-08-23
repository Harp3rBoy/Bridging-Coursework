from django.shortcuts import redirect, render
from .models import PersonalDetails
from .forms import DetailsForm


def home_page(request):
    return render(request, 'cv/base.html')


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

