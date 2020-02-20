from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
    helper.form_method = 'POST'
