from django import forms
from django.core.exceptions import ValidationError


widget_textarea = forms.Textarea(
    # cssを適用させる
    attrs={"class": "form-control"}
)

widget_textinput = forms.TextInput(attrs={"class": "form-control"})


class TextForm(forms.Form):
    text = forms.CharField(label="", widget=widget_textarea)
    search = forms.CharField(label="検索", widget=widget_textinput)
    replace = forms.CharField(label="置換", widget=widget_textinput)

    def clean(self):
        data = super().clean()  # views.pyのdata(= form.cleaned_data)を呼び出す
        text = data["text"]
        # textが5文字以下の時にエラーを発生させる
        if len(text) <= 5:
            raise ValidationError("テキストが短すぎます。6文字以上入力してください。")
        return data
