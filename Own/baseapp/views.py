from django.shortcuts import render,redirect,render_to_response
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView,TemplateView
from . import forms
from django.http import HttpRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from baseapp.forms import Pictures_Form,PostForm,Profile_Form,NoticesForm,LectorsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from baseapp.models import Post,Pictures,Profile_pic,Notices,Lectors
from django.urls import reverse_lazy,reverse
from django.forms import modelformset_factory
from django.shortcuts import render, get_object_or_404
from django.contrib import messages


# Create your views here.

class timing(TemplateView):
    template_name="baseapp/timings.html"

class History(TemplateView):
    template_name="baseapp/history.html"

# picture Model.

def Pictures_View(request):
        if request.method=='POST':

            user_form = Pictures_Form(request.POST,request.FILES)
            if user_form.is_valid():
                for field in request.FILES.keys():
                    for formfile in request.FILES.getlist(field):
                        church_pic = Pictures(church_pic=formfile)
                        church_pic.save()
                return redirect('pictures:post_list')
        else:
            user_form = Pictures_Form()
        return render(request,'baseapp/pictures_up.html',{'user_form':user_form})

        def main(request):
            i = get_object_or_404(Image, pk=1)
            return render_to_response('baseapp/post_list.html', {'image': i}, context_instance=RequestContext(request))


class PostListView(ListView):
        model=Post
        template_name="baseapp/post_list.html"

        # def get_queryset(self):
        #     return Post.objects.filter(create_date__lte=timezone.now()).order_by('-create_date')


class PostDetailView(DetailView):
        model = Post

class CreatePostView(LoginRequiredMixin,CreateView):
        login_url = '/login/'
        redirect_field_name = 'baseapp/post_detail.html'
        form_class = PostForm
        model = Post

class UpdatePostView(LoginRequiredMixin,UpdateView):
        login_url = '/login/'
        redirect_field_name = 'baseapp/post_detail.html'
        form_class = PostForm
        model = Post

class DeletePostView(LoginRequiredMixin,DeleteView):
        model = Post
        success_url = reverse_lazy('pictures:post_list')

def ContactView(request):
        # mapbox_access_token = 'pk.my_mapbox_access_token'
        return render(request, 'baseapp/contact_us.html')


def SaveNotices(request):
    notice_fr = NoticesForm()
    if request.method == 'POST':
        notice_fr = NoticesForm(request.POST, request.FILES)
        if notice_fr.is_valid():
            user_pr = notice_fr.save(commit=False)
            user_pr.file = request.FILES['file']
            user_pr.save()
        return redirect('pictures:notices_list')
    context = {"notice_fr": notice_fr,}
    return render(request, 'baseapp/notices.html', context)



class NoticesListView(ListView):
        model = Notices



def delete_file(request, pk):
        if request.method == 'POST':
            notices = Notices.objects.get(pk=pk)
            notices.delete()
        return redirect('pictures:notices_list')


def NewProfile(request):

        profile_fr = Profile_Form()
        if request.method == 'POST':
            profile_fr = Profile_Form(request.POST, request.FILES)
            if profile_fr.is_valid():
                prof_pr = profile_fr.save(commit=False)
                prof_pr.Parishpriest_pic = request.FILES['Parishpriest_pic']
                prof_pr.save()
            return redirect('pictures:post_list')
        context = {"profile_fr": profile_fr,}
        return render(request, 'baseapp/profile_pic_form.html', context)



def delete_profile_p(request, pk):
    if request.method == 'POST':
        profile_p = Profile_pic.objects.get(pk=pk)
        profile_p.delete()
    return redirect('pictures:profile_pic_list')


def UpdateProfile(request, pk, template_name='baseapp/profile_pic_form.html'):
        profile_pic = get_object_or_404(Profile_pic, pk=pk)
        profile_fr = Profile_Form(request.POST or request.FILES or None, instance=profile_pic)
        if profile_fr.is_valid():
            prof_pr = profile_fr.save(commit=False)
            prof_pr.Parishpriest_pic = request.FILES['Parishpriest_pic']
            prof_pr.save()
            return redirect('pictures:profile_pic_list')
        return render(request, template_name, {'profile_fr':profile_fr})

class NewProfListView(ListView):
        model=Profile_pic

class ParishCouncil(TemplateView):
    template_name= "baseapp/parish_council.html"

class ChurchStaff(TemplateView):
        template_name="baseapp/church_staff.html"

class OfficeTimings(TemplateView):
        template_name="baseapp/office_timings.html"

class Zone(TemplateView):
        template_name="baseapp/zone.html"

class Confessions(TemplateView):
    template_name="baseapp/confession.html"


def SaveLectors(request):
    lectors_fr = LectorsForm()
    if request.method == 'POST':
        lectors_fr = LectorsForm(request.POST, request.FILES)
        if lectors_fr.is_valid():
            user_pr = lectors_fr.save(commit=False)
            user_pr.file = request.FILES['file']
            user_pr.save()
        return redirect('pictures:lectors_list')
    context = {"lectors_fr": lectors_fr,}
    return render(request, 'baseapp/lectors.html', context)

class LectorsListView(ListView):
        model = Lectors

def delete_lectors(request, pk):
        if request.method == 'POST':
            lectors = Lectors.objects.get(pk=pk)
            lectors.delete()
        return redirect('pictures:lectors_list')
