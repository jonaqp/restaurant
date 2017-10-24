from django.views.generic import TemplateView

from project_name.apps.core.mixins import TemplateLoginRequiredMixin


class IndexView(TemplateLoginRequiredMixin):
    template_name = 'themes/pages/home/home.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
