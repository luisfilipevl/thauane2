from django import forms
from .models import *

class NoticiaForm(forms.ModelForm):
    
    class Meta:
        model = Noticia
        fields = '__all__'
        widgets = {
            'data_publicacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), 
            'texto': forms.Textarea(attrs={'class': 'form-control'}),  
            'titulo': forms.TextInput(attrs={'class': 'form-control'}), 
            'image': forms.FileInput(attrs={'class': 'form-control'}), 
            'Voo': forms.Select(attrs={'class': 'form-control'}),

        }

class VooForm(forms.ModelForm):
    
    class Meta:
        model = Voo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}), 
            

        }



from django import forms
from .models import Voo
from usuarios.models import UserBlog  # Importe o modelo de usuário personalizado

class NoticiaFilterForm(forms.Form):
    titulo = forms.CharField(
        max_length=200,
        required=False,
        label='Título',
        widget=forms.TextInput(attrs={'placeholder': 'Digite o título','class': 'form-control'})
    )
    data_publicacao_inicio = forms.DateField(
        required=False,
        label='Data de Publicação (Início)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    data_publicacao_fim = forms.DateField(
        required=False,
        label='Data de Publicação (Fim)',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    Voo = forms.ModelChoiceField(
        queryset=Voo.objects.all(),
        required=False,
        label='Voo',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class VooFilterForm(forms.Form):
    nome = forms.CharField(
        max_length=200,
        required=False,
        label='Nome',
        widget=forms.TextInput(attrs={'placeholder': 'Digite o nome','class': 'form-control'})
    )