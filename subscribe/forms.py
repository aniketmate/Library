from django import forms

class Subscribe(forms.Form):
    email = forms.CharField()

    # def __str__(self):
    #     return self.email

s = Subscribe()
print(s)
