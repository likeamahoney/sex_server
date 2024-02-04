from django import forms

PSYCHO_CHOICES =( 
    ("Уеба", "Уеба"), 
    ("Уебан", "Уебан"), 
    ("Шлюха", "Шлюха"), 
    ("Тварь и хуйло", "Тварь и хуйло"), 
)
 
class RegisterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        name = kwargs.pop("name") if "name" in kwargs else None
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["name"] = forms.CharField(label="Имя", initial = "Я знаю ты уеба") if name is None else forms.CharField(label="Имя", initial = name, widget=forms.HiddenInput())
        self.fields["psycho_types"] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PSYCHO_CHOICES, label="Ваши психотипы (выберите несколько)", initial = ("Уеба", "Уеба"))
        if name is not None:
            self.fields["edit"] = forms.CharField(initial = "edit", widget=forms.HiddenInput())

#class EditForm(forms.Form):
#    psycho_types = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PSYCHO_CHOICES, label="Ваши психотипы (выберите несколько)", initial = ("Уеба", "Уеба"))
