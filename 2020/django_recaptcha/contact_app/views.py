import requests
from django.conf import settings
from django.shortcuts import render
from django.views import generic
from . import forms

class Contact(generic.FormView):
    template_name = 'contact.html'
    form_class = forms.ContactForm
    success_url = ''
    extra_context = {
        'recaptcha_key': settings.RECAPTCHA_PUBLIC_KEY
    }

    def form_valid(self, form):
        print(self.request.POST)
        token = self.request.POST['g-recaptcha-response']
        print(token)
        if token:
            print(token)
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': token
            }
            request = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data = data
            )
            print(request)
            result = request.json()
            print(result)
            if result['success'] and result['score'] >= 0.5:
                form.save()
        return render(self.request, 'contact.html', {
            'form': self.get_form(),
            'message': 'Thank you'
        })
