from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
class HomeView(LoginRequiredMixin, TemplateView):
    """
    HomePage class
    """
    template_name = 'home.html'
    