from django.shortcuts import redirect
from django.urls import reverse

from .mixins import TemplateLoginRequiredMixin


class IndexView(TemplateLoginRequiredMixin):
    template_name = 'themes/pages/home/home.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        else:
            return redirect(reverse("core_app:home"))

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomeView(TemplateLoginRequiredMixin):
    template_name = 'themes/pages/home/home.html'

    def get(self, request, *args, **kwargs):
        return super().render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
