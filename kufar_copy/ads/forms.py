from django import forms
from .models import Ad, Category

class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category', 'image']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Подробно опишите товар или услугу'
            }),
            'category': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'image': 'Загрузите фото (макс. 5 МБ)'
        }

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля")
        return price


class AdCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Категория",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Выберите категорию'
        }),
        empty_label="Не выбрано"
    )

    class Meta:
        model = Ad
        fields = ['title', 'description', 'price', 'category', 'image']