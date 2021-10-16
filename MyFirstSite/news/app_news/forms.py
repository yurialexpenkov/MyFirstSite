

from django import forms
from app_news.models import News, MyComment



class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        exclude = ('status_verifications', 'activity', 'user')

class MyCommentForm(forms.ModelForm):

    class Meta:
        model = MyComment
        exclude = ('news', 'user')

class MyCommentAuthenticatedForm(forms.ModelForm):

    class Meta:
        model = MyComment
        exclude = ('news', 'user', 'user_name')