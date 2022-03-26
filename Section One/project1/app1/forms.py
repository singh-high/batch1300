from django import forms

from django.core import validators

def batch22(value):
    if value[0:2] != '22' :
        raise forms.ValidationError("Only batch 2022 is allowed")

class FormName(forms.Form):
    roll_number = forms.CharField(validators=[batch22])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label="enter your mail again")
    text = forms.CharField(widget=forms.Textarea)
    # bot = forms.CharField(required = False,widget = forms.HiddenInput )

    # def clean_bot(self):
    #     bot = self.cleaned_data['bot']
    #
    #     if len(bot) > 0:
    #         raise forms.ValidationError("Bot recognized")
    #     return bot

    def clean(self):
        all_data = super().clean()
        email = all_data['email']
        vmail = all_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Email doesn't match")