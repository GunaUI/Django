from django import forms
from django.core import validators
from first_app.models import User

# Custom class validation for form

def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("Name needs to be start with Z !")
class FormName(forms.Form):
	# name = forms.CharField(validators=[check_for_z])
	name = forms.CharField()
	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label='Enter email again')
	text = forms.CharField(widget=forms.Textarea)
	# botcather = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	# Custom form Validation

	# def clean_botcather(self):
	# 	botcather = self.cleaned_data['botcather']
	# 	if len(botcather) > 0 :
	# 		raise forms.ValidationError("GOTCHA BOT!")
	# 	return botcather

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vemail = all_clean_data['verify_email']

		if email!=vemail:
			raise forms.ValidationError("Make Sure Email Match!")

class NewUserForm(forms.ModelForm):
	"""here you can do form validation like below"""
	"""name = forms.CharField(validators=[check_for_z])"""	
	class Meta():
		"""Meta definition for MODELNAMEform."""
		model = User
		fields = '__all__'
