# Django
## Basic Forms 
* The first thing we need to do is create a forms.py file inside the application! 
* After that we call Django’s built in forms classes (looks very similar to creating models).
    ```
    from django import forms
    from django.core import validators

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
    ```
* Form HTML

    ```
    <form method="POST">
        {{form.as_p}}
        {% csrf_token %}
        <input type="submit" class="btn btn-primary" value="Submit"/>
    </form>
    ```
#### Next Branch : django-model-forms

