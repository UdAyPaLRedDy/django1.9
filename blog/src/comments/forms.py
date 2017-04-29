from django import forms

class CommentForm(forms.Form):
	Comment_type = forms.CharField(widget=forms.HiddenInput)
	object_id = forms.IntegerField(widget=forms.HiddenInput)
	content = forms.CharField(label='', widget=forms.Textarea)