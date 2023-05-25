from django import forms
from django.core.exceptions import ValidationError


class TextForm(forms.Form):
    text = forms.CharField()
    search = forms.CharField()
    replace = forms.CharField()

    def clean(self):
        data = super().clean()  # views.pyのdata(= form.cleaned_data)を呼び出す
        text = data["text"]
        # textが5文字以下の時にエラーを発生させる
        if len(text) <= 5:
            raise ValidationError("テキストが短すぎます。6文字以上入力してください。")
        return data
