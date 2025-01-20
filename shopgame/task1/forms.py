from django import forms
from task1.user_name import users

class UserRegister(forms.Form):
    username = forms.CharField(label='Введите логин', max_length=30)
    password = forms.CharField(label='Введите пароль', min_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label='Повторите пароль', min_length=8, widget=forms.PasswordInput)
    age = forms.IntegerField(label='Введите свой возраст', min_value=1, max_value=999)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')
        age = cleaned_data.get('age')
        username = cleaned_data.get('username')

        if password != repeat_password:
            raise forms.ValidationError('Пароли не совпадают')
        if age < 18:
            raise forms.ValidationError('Вы должны быть старше 18')
        if username in users:
            raise forms.ValidationError('Пользователь уже существует')

        return cleaned_data