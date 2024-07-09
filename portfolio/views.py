from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView

from portfolio.forms import ContactForm
from portfolio.models import Project


def home(request):
    return render(request, 'portfolio/index.html', {'active_page': 'home'})


def portfolio_view(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'active_page': 'portfolio'

    }
    return render(request, 'portfolio/portfolio.html', context)


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'portfolio/contact.html'
    success_url = reverse_lazy('home')
    title_page = 'Обратная связь'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'contact'
        return context

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        subject = f"Новое сообщение от {name}"
        email_message = f"""
                Имя: {name}
                Email: {email}
                Сообщение:
                {message}
                """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL]

        send_mail(subject, email_message, from_email, recipient_list)

        return super().form_valid(form)