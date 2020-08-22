from django.shortcuts import redirect, render
from cv.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/cv')

    items = Item.objects.all()
    return render(request, 'cv/base.html', {'items': items})
