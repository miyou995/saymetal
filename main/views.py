from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.views.generic import ListView, DetailView, FormView, View
from django.contrib import messages

from .forms import  ContactForm
from .models import Product, Reference



# Create your views here.
class HomeView(View):
    template_name = 'index.html'

    # model = Produit

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["produit"] = Produit.objects.all()
    #     return context

def home(request):
    return render(request, 'index.html')


class ProductListView(ListView):
    model = Product

    context_object_name = 'products'
    template_name='products.html'

class ReferencesListView(ListView):
    model = Reference

    context_object_name = 'references'
    template_name='about.html'

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = "/contact"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
    
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')
            honeypot = form.cleaned_data['honeypot']

            body = 'Nom: {} \n email: {} \n Phone:{} \n Sujet: {} \n Message: {}' .format(name, email, phone, subject, message)
            mail = EmailMessage('Cet email est envoyer depuis le site internet', body, 'inter.taki@gmail.com', ['inter-95@hotmail.fr']) 
            mail.send()
            messages.success(request, 'Votre message a bien été envoyer')
        return redirect('/contact')

        # return render(request, self.template_name, {'email_form': form, 'error_message': "Votre message n'a pas été envoyer, réessayez plus tard "})





