from django.shortcuts import render

from .forms import ImageForm

from .models import Image 

def showimage(request):
    lastimage = Image.objects.last()
    imagefile= lastimage.imagefile
    form= ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context= {'imagefile': imagefile,
              'form': form
              } 
    return render(request, 'hotel_image_form.html.html', context)