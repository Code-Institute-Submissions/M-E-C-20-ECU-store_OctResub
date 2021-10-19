from django.shortcuts import render
from django.contrib import messages
from .models import Contact

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


def contact_admin(request):
    """ A view to show all contact requests, including sorting queries """

    contacts = Contact.objects.all()

    context = {
        'contacts': contacts,
    }

    return render(request, 'contact/contact_admin.html', context)
