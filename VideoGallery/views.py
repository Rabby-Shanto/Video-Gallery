from django.shortcuts import render
from UserGallery.models import PlayList





def home(request):
    if request.user.is_authenticated:


        playlist = PlayList.objects.filter(user=request.user)
        context = {
            'playlist' : playlist
        }
        return render(request,'home.html',context)
    return render(request,'home.html')
    