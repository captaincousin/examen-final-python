from django import forms
from apps.meseros.models import Meseros

class MeserosForm(forms.ModelForm):
    class Meta:
        model = Meseros
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"