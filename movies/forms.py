from movies.models import VideoComment
from django import forms


class CommentForm(forms.ModelForm):
	text = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': ''}))

	class Meta:
		model = VideoComment
		fields = ['text']
