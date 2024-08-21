import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

logger = logging.getLogger("custom_logger")

class HomeView(LoginRequiredMixin, TemplateView):
    """
    HomePage class
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logger.debug(context)
        return context
    