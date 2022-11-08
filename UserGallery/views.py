from django.shortcuts import render

# Create your views here.

def u_gallery(request):
    return render(request,'gallery/user_gallery.html')
