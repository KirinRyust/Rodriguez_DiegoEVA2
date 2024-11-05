from django import forms # type: ignore
from rodriguez_diegoEVA2APP.models import Seminario

class FormSeminario(forms.ModelForm):
    class Meta:
        model = Seminario
        fields = '__all__'