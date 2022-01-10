from django import forms
from ca_and_news.models import Blog

class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','body','thumb')