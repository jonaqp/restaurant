from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'themes/dashboard/test.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

