from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.http import Http404,HttpResponse,JsonResponse
from .models import PlayList,Video
from .forms import AddvideoForm,SearchvideoForm
from django.contrib import messages
import urllib
import requests
from django.conf import settings

YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY
# https://youtube.googleapis.com/youtube/v3/search?part=snippet&relatedToVideoId=3QNBVG2yqKA&type=video&key=[YOUR_API_KEY]
# https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id=3QNBVG2yqKA&key=[YOUR_API_KEY]
# https://youtube.googleapis.com/youtube/v3/search?part=snippet&q=eggs&key=[YOUR_API_KEY]

# Create your views here.

def video_search(request):
    search_form = SearchvideoForm(request.GET)
    if search_form.is_valid():
        search = search_form.cleaned_data['search_term']
        encoded_search_term = urllib.parse.quote(search)
        response = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&q={encoded_search_term}&key={YOUTUBE_API_KEY}')

        return JsonResponse(response.json())

    return JsonResponse({'Sorry':'Not Working'})


@login_required
def u_gallery(request):
    playlists = PlayList.objects.filter(user=request.user)
 


    context = {

        'playlists': playlists,

    }


    return render(request,'gallery/user_gallery.html',context)


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

@method_decorator(login_required,name='dispatch')
class detail_view(generic.DetailView):
        model = PlayList
        template_name = 'gallery/detail_playlist.html'
        def get_context_data(self, **kwargs):

            context = super().get_context_data(**kwargs)

            context['videos'] = Video.objects.filter(playlist__user=self.request.user,playlist__id=self.kwargs.get('pk'))
            return context


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



@login_required
def add_video(request,pk):

    playlist = PlayList.objects.get(pk=pk)

    if not playlist.user == request.user:
        return HttpResponse("Playlist doesn't belongs to you")

    else:

        form = AddvideoForm()
        search_form = SearchvideoForm()

        if request.method == 'POST':

            video_form = AddvideoForm(request.POST)

            if video_form.is_valid():
                video = Video()
                video.playlist = playlist
                video.url = video_form.cleaned_data['url']
                parsed_url = urllib.parse.urlparse(video.url)
                video_id = urllib.parse.parse_qs(parsed_url.query).get('v')

                if video_id:

                    video.youtube_id = video_id[0]
                    if Video.objects.filter(youtube_id=video.youtube_id,playlist=video.playlist.id).exists():
                        messages.error(request,'Video already exists in your playlist!')

                    else:

                        response = requests.get(f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={video_id[0]}&key={YOUTUBE_API_KEY}')
                        json = response.json()
                        title = json['items'][0]['snippet']['title']
                        video.title = title
                        video.save()

                else:
                    
                    messages.error(request,"Not a youtube url")
        context = {'form' : form,'search_form': search_form,'playlist' : playlist}
        return render(request,'gallery/add_video.html',context)


@method_decorator(login_required, name='dispatch')
class delete_video(generic.DeleteView):
    model = Video
    template_name  = 'gallery/delete_video.html'
    success_url = reverse_lazy('u_gallery')



