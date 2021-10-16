from django.contrib.auth.decorators import permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from app_news.models import News, MyComment
from django.views import View, generic
from app_news.forms import NewsForm, MyCommentForm, MyCommentAuthenticatedForm

class NewsFormView(View):


    def get(self, request):
        if request.user.has_perm('app_news.add_news'):
            news_form = NewsForm()
            return render(request, 'news/create.html', context={'news_form': news_form})
        else:
            return HttpResponseRedirect('/news')

    def post(self, request):
        news_form = NewsForm(request.POST)

        if news_form.is_valid():
            if request.user.has_perm('app_news.can_publish'):
                News.objects.create(**news_form.cleaned_data, user=request.user, status_verifications='a')
                request.user.profile.count_of_news += 1
            else:
                News.objects.create(**news_form.cleaned_data, user=request.user)
            request.user.profile.save()

            return HttpResponseRedirect('/news/create')
        return render(request, 'news/create.html', context={'news_form': news_form})

class MyCommentFormView(View):

    def get(self, request):
        if request.user.is_authenticated:
            comment_form = MyCommentAuthenticatedForm()
        else:
            comment_form = MyCommentForm()
        return render(request, 'news/news_detail.html', context={'comment_form': comment_form})

    def post(self, request, profile_id):
        news = News.objects.get(id=profile_id)
        if request.user.is_authenticated:
            comment_form = MyCommentAuthenticatedForm(request.POST)
            if comment_form.is_valid():
                MyComment.objects.create(**comment_form.cleaned_data, news=news, user=request.user, user_name=request.user.username)
                return HttpResponseRedirect(f'/news/{profile_id}')
        else:
            comment_form = MyCommentForm(request.POST)
            print(request.user)
            if comment_form.is_valid():
                MyComment.objects.create(**comment_form.cleaned_data, news=news)
                return HttpResponseRedirect(f'/news/{profile_id}')
        return render(request, 'news/news_detail.html', context={'comment_form': comment_form})

class NewsEditFormView(View):
    def get(self, request, profile_id):
        if request.user.has_perm('app_news.add_news'):
            user = News.objects.get(id=profile_id)
            news_form = NewsForm(instance=user)
            return render(request, 'news/edit.html', context={'news_form': news_form, 'profile_id': profile_id})
        else:
            return HttpResponseRedirect('/news')


    def post(self, request, profile_id):
        news = News.objects.get(id=profile_id)
        news_form = NewsForm(request.POST, instance=news)
        if news_form.is_valid():
            news.save()
        return render(request, 'news/edit.html', context={'news_form': news_form, 'profile_id': profile_id})

class NewsListView(generic.ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perm'] = self.request.user.has_perm('app_news.add_news')
        print(context['perm'])
        return context



class NewsDetailView(generic.DetailView):
    model = News
    template_name = 'news/news_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = MyComment.objects.all()
        context['comment_form'] = MyCommentForm()
        context['comment_form_authenticated'] = MyCommentAuthenticatedForm()
        return context

def response_to_search(request, *args, **kwargs):
    description = request.POST['search']
    news_list = News.objects.filter(status_verifications="a", title__icontains=description)
    perm = request.user.has_perm('app_news.add_news')
    return render(request, 'news/response_to_search.html', {'news_list': news_list, 'perm': perm})





