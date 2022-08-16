from django import forms

from urlapp.models import Link

class LinksCreateForm(forms.ModelForm):
	links_title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Group of links name',
    }))
	url = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Insert urls without any separators (only enter)',
		'rows': 3
    }))

	def __init__(self, data=None, request=None) -> None:
		super().__init__(data)
		self.request = request

	class Meta:
		model = Link
		fields = ("links_title", "url")

	def clean(self):
		unsupported_characaters = (",", ";", "|")
		for characters in unsupported_characaters:
			if characters in self.cleaned_data["url"]:
				self._errors['url'] = self.error_class(['Invalid separator'])
				
		return self.cleaned_data

	def save(self, commit=True):
		return Link.objects.create(user=self.request.user, **self.cleaned_data)