from django import forms

class CreateTeamForm(forms.Form):

    team_name = forms.CharField()
    team_description = forms.CharField(widget=forms.Textarea)