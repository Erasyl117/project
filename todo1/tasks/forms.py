from django import forms
class UserForm(forms.Form):
    name=forms.CharField(label='Имя',max_length=15,min_length=3,required=True)
    email=forms.EmailField(label='Email',required=False)
    password=forms.CharField(widget=forms.PasswordInput,min_length=8,max_length=36,required=True)
    # date=forms.IntegerField(label='Дата рождения',min_value=15,max_value=50)
    # file=forms.FileField(label='Выберите файл',help_text="Выберите тот файл который вы хотите загрузить")
    # age=forms.IntegerField(label='Возраст')
    # lang=forms.ChoiceField(
    #     choices=[('java','java'),
    #              ('python','python'),
    #              ('html','html'),])
    required_css_class='field'
    error_css_class='error'
  