from .models import template

class PhotoForm(forms.ModelForm):
    class Meta:
        model = template
        fields = ('file', )