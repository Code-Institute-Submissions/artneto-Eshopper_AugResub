from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    """
    form for managing crud for blogs
    """
    class Meta:
        model = Contact
        fields = '__all__'
