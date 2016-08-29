from django.shortcuts import render
from photologue.models import Photo
from django.shortcuts import get_object_or_404
# Create your views here.


def index(request):
    queryset = Photo.objects.on_site().is_public()
    context = {
        "photos": queryset
    }
    return render(request, 'photologue/photo_list.html', context)
