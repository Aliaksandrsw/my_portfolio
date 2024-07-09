from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ИМЯ',
            'id': 'name',
            'style': 'font-size: 16px;'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'EMAIL',
            'id': 'email',
            'style': 'font-size: 16px;'
        })
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'СООБЩЕНИЕ',
            'rows': '5',
            'id': 'message',
            'style': 'font-size: 16px;'
        })
    )
