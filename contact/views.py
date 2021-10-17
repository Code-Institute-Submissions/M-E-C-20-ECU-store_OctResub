from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your enquiry. A member of our team will be in touch soon!')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    form = ContactForm()
    context = {'form': form}
    template = 'contact/contact.html'
    return render(request, template, context)
