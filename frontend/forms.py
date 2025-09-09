from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import User, Userinfo, Review, Country
from .models import RequestsData , ContactData

# Registration Form
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your last name"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    country = forms.ModelChoiceField(
    queryset=Country.objects.filter(is_deleted=False),
    widget=forms.Select(attrs={"class": "form-control"}),
    required=True,
    )

    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'class':'form-control'}), required=False)
    is_maried = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'country', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.country = self.cleaned_data['country']
        if commit:
            user.save()
            Userinfo.objects.create(
                user=user,
                birthdate=self.cleaned_data.get('birthdate'),
                address=self.cleaned_data.get('address'),
                is_maried=self.cleaned_data.get('is_maried', False)
            )
        return user

# Login Form
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'autofocus': True}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


# Review Form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['product', 'review', 'rating', 'is_positive']
        widgets = {
            'review': forms.Textarea(attrs={'rows': 3}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }


# Requests Form
class RequestsForm(forms.ModelForm):
    class Meta:
        model = RequestsData
        fields = ['car', 'name', 'mobile_phone', 'language', 'payment_method']


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactData
        fields = ['subject', 'name', 'email', 'message']
