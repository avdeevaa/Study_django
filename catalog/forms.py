from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ('owner',)  # это позволит выставить значение автоматически

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in self.bad_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Ошибка, такое слово добавить нельзя.')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in self.bad_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Ошибка, такое слово добавить нельзя.')

        return cleaned_data