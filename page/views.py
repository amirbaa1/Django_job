from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from Company.models import Company, Job


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact_us.html'


class jobView(TemplateView):
    template_name = 'job.html'


class storeView(TemplateView):
    template_name = 'store.html'


class HomeView(TemplateView):
    def get(self, request):
        companies = Company.objects.all()
        jobs = Job.objects.all()
        context = {
            'comp2': companies,
            'job_li': jobs,
        }
        return render(request, 'home.html', context)


class ListCompany(ListView):
    model = Company
    template_name = 'home.html'
    context_object_name = 'comp2'
