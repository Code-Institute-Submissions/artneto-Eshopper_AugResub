from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(min_length=3,
                           max_length=100, label='Name',
                           widget=forms.TextInput())

    email = forms.EmailField(widget=forms.EmailInput(),
                             label='Your Email Address')
    subject = forms.CharField(min_length=3,
                              max_length=40, label='Subject',
                              widget=forms.TextInput())
    message = forms.CharField(min_length=5,
                              max_length=40,
                              widget=forms.Textarea(), label='Message')
