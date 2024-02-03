from django import forms

PSYCHO_CHOICES =( 
    ("Уеба", "Уеба"), 
    ("Уебан", "Уебан"), 
    ("Шлюха", "Шлюха"), 
    ("Тварь и хуйло", "Тварь и хуйло"), 
)
 
class RegisterForm(forms.Form):
    name = forms.CharField(label="Имя", initial = "Я знаю ты уеба")
    psycho_types = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PSYCHO_CHOICES, label="Ваши психотипы (выберите несколько)", initial = ("Уеба", "Уеба"))

class EditForm(forms.Form):
    psycho_types = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PSYCHO_CHOICES, label="Ваши психотипы (выберите несколько)", initial = ("Уеба", "Уеба"))
