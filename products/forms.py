from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms


class ChangeProductValue(forms.Form):
    product_value = forms.IntegerField(
            help_text="Введите количество продукта")

    def clean_product_value(self):
        data = self.cleaned_data['product_value']

        # Check value is > 0.
        if data < 0:
            raise ValidationError(_('Количество продукта не может быть отрицательным'))

        # Remember to always return the cleaned data.
        return data
