from django.http import HttpResponse
from django.views.generic.edit import FormView

from . import forms


class Index(FormView):
    form_class = forms.TextForm
    template_name = "index.html"

    # 入力されたデータに問題がない場合呼ばれる関数
    def form_valid(self, form) -> HttpResponse:
        data = form.cleaned_data  # 入力されたデータ(辞書型)
        text = data["text"]
        search = data["search"]
        replace = data["replace"]

        # textの中のsearchをreplaceに変換
        new_text = text.replace(search, replace)

        # テンプレートに渡す
        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_response(ctxt)
