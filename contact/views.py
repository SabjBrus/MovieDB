from django.views.generic import CreateView

from contact.models import Contact
from contact.forms import ContactForm


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    