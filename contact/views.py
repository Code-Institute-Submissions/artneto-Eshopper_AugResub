from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact(request):
    """
    View to submit contact form for contact.html
    """
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

            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Message not sent please try again.')
    else:
        form = ContactForm()

    template = 'contact_us/contact.html'
    context = {
        'form': form,

    }

    return render(request, template, context)