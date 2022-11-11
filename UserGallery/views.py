from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from .models import PlayList
from .forms import AddvideoForm,SearchvideoForm


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

    def form_valid(self, form):
        form.instance.user=self.request.user
        super(create_playlist,self).form_valid(form)
        return redirect('u_gallery')

@method_decorator(login_required, name='dispatch')
class detail_view(generic.DetailView):
        model = PlayList
        template_name = 'gallery/detail_playlist.html'


@method_decorator(login_required, name='dispatch')
class update_playlist(generic.UpdateView):
    model = PlayList
    fields = ['title']
    template_name  = 'gallery/update_playlist.html'
    success_url = reverse_lazy('u_gallery')


@method_decorator(login_required, name='dispatch')
class delete_playlist(generic.DeleteView):
    model = PlayList
    template_name  = 'gallery/delete_playlist.html'
    success_url = reverse_lazy('u_gallery')


def add_video(request,pk):
        form = AddvideoForm()
        search_form = SearchvideoForm()
        context = {'form' : form,'search_form': search_form}
        return render(request,'gallery/add_video.html',context)