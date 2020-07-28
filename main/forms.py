from .models import Circle
from django.forms import ModelForm, TextInput

class CircleForm(ModelForm):
    class Meta:
        model = Circle
        styl = "margin: 10px 0px"
        fields = ["x", "y", "r"]
        widgets = {
            'x': TextInput(attrs={
                'placeholder': "Введите Х",
                'style': styl
            }),
            'y': TextInput(attrs={
                'placeholder': "Введите Y",
                'style': styl
            }),
            'r': TextInput(attrs={
                'placeholder': "Введите R",
                'style': styl
            })
        }