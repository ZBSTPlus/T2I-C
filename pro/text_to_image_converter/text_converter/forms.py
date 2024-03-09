from django import forms
from .models import TextToImage

class TextToImageForm(forms.ModelForm):
    class Meta:
        model = TextToImage
        fields = ['text', 'font_size']
