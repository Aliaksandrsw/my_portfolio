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
        return super().form_valid(form)
