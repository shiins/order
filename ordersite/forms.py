from django import forms
from .models import Offer

class PostForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('購入者', 'メールアドレス', '品名', 'サイズ', '価格', '数量')

PostFormSet = forms.modelformset_factory(
    Offer, form=PostForm, extra=10,
)
