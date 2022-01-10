from stories.models import Story
from django import forms

class AddStoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('content',)