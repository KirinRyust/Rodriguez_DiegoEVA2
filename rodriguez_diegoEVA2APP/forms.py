from django import forms # type: ignore
from rodriguez_diegoEVA2APP.models import Django_Seminario

class FormSeminario(forms.ModelForm):
    class Meta:
        model = Django_Seminario
        fields = '__all__'