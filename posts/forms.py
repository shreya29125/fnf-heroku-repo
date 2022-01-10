from posts.models import Post, Comment
from django import forms

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('caption', 'file', 'tags', 'thumbnail')
        help_texts = {'tags': "Use Tags as continuous, with '#' at the beginning, and each tag separated by a single space",
                        'thumbnail': "Thumbnails can be uploaded for the video and audio type posts"}
    
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content','post')
        widgets = {'post': forms.HiddenInput()}

class SharePostForm(forms.Form):
    caption = forms.CharField()
    post = forms.CharField(widget = forms.HiddenInput(), required = True)
    