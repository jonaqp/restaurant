from .mixins import TemplateLoginRequiredMixin


class IndexView(TemplateLoginRequiredMixin):
    template_name = 'themes/pages/home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
