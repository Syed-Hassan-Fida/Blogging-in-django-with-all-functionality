from django import forms

class signup(forms.Form):
    username = forms.CharField(max_length = 20, required = True)
    password = forms.CharField(widget = forms.PasswordInput)
    
    #Validation #DataFlair
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 4:
            raise forms.ValidationError("password is too short")
        return password