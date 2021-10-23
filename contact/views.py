from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm


def contact_view(request):
    """ A view to handle the contact form """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your enquiry. A member of our team will be in touch soon!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    form = ContactForm()
    context = {'form': form}
    template = 'contact/contact.html'
    return render(request, template, context)


@login_required
def contact_admin(request):
    """ A view to show all contact requests, including sorting queries """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    else:
        contacts = Contact.objects.all().order_by('-created')

        context = {
            'contacts': contacts,
        }

        return render(request, 'contact/contact_admin.html', context)


@login_required
def contact_message(request, contact_id):
    """ A view to show an individual contact message """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    else:
        contact = get_object_or_404(Contact, pk=contact_id)

        context = {
            'contact': contact,
        }
        template = 'contact/contact_message.html'

        return render(request, template, context)


@login_required
def delete_contact(request, contact_id):
    """ Delete a contact from the contact admin """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    contact = get_object_or_404(Contact, pk=contact_id)
    contact.delete()
    messages.success(request, 'Message deleted!')
    return redirect(reverse('contact_admin'))
