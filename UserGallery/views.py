from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
from .models import PlayList
from django.urls import reverse_lazy
# Create your views here.
@login_required
def u_gallery(request):

        return render(request,'gallery/user_gallery.html')


@method_decorator(login_required, name='dispatch')
class create_playlist(generic.CreateView):
    model = PlayList
    fields = ['title']
    template_name  = 'gallery/create_playlist.html'
    success_url = reverse_lazy('u_gallery')


