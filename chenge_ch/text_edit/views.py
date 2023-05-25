from django.views.generic.edit import FormView

from . import forms


class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"
