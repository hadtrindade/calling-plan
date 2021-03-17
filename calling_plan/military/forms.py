from django import forms
from .models import Military


class MilitaryForm(forms.ModelForm):

    class Meta:
        model = Military
        fields = '__all__'

        widgets = {
            "identidade": forms.TextInput(attrs={"class": "form-control"}),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "graduacao": forms.Select(attrs={"class": "form-control"}),
            "subunidade": forms.Select(attrs={"class": "form-control"}),
            "operacional": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "telefone": forms.TextInput(attrs={"class": "form-control"}),
            "telefone_familia": forms.TextInput(attrs={"class": "form-control"}),
            "telefone_telegram": forms.TextInput(attrs={"class": "form-control"}),
            "telefone_whatsapp": forms.TextInput(attrs={"class": "form-control"}),
            "chamador": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "rua": forms.TextInput(attrs={"class": "form-control"}),
            "bairro": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "estado": forms.TextInput(attrs={"class": "form-control"}),
            "cep": forms.TextInput(attrs={"class": "form-control"}),
            "area": forms.Select(attrs={"class": "form-control"}),
        }
