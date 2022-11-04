from django.views.generic.base import TemplateView


class AboutAuthor(TemplateView):
    template_name = 'about/author.html'
