"""Views for 'contact' app"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        user_message = request.POST.get('message')
        subject = request.POST.get('subject')
        if form.is_valid():
            form.save()
            # sending email to admin following a contact form submission
            send_mail(
                subject,
                user_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,)

            messages.success(request, 'We have received your email!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Wrong request, please try again.')
    else:
        form = ContactForm()

    template = 'contact_us/contact.html'
    context = {
        'form': form,

    }

    return render(request, template, context)
