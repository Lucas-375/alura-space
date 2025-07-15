from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Carlota Bolota'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Carlota Bolota'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex: jelson@xpto.com'
            }
        )
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    senha_2 = forms.CharField(
        label='Confirme sua senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços são invalidos no nesse campo', code='warning')    
            else:
                return nome

    def clean_senha_2(self):      
        senha_1 = str(self.cleaned_data.get('senha_1'))
        senha_2 = str(self.cleaned_data.get('senha_2'))

        if senha_1 and senha_2:
            import string

            if senha_1 != senha_2:
                raise forms.ValidationError('As senhas nao são iguais')
            if not any(c.isalpha() for c in senha_2):
                raise forms.ValidationError('A senha deve conter ao menos uma letra', code='warning')
            if not any(c.isdigit() for c in senha_2):
                raise forms.ValidationError('A senha deve conter ao menos um número', code='warning')
            if not any(c in string.punctuation for c in senha_2):
                raise forms.ValidationError('A senha deve conter ao menos um símbolo', code='warning')
            else:
                return senha_2