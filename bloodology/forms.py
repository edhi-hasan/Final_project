from django import forms 
from .models import BloodRequestPost, UserProfile,BlogPost
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm , UsernameField 
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy as _
from tinymce.widgets import TinyMCE

class RequestPostForm(forms.ModelForm):
    class Meta:
        model = BloodRequestPost
        fields = ['blood_group', 'date_time', 'Disease_name', 'No_of_bag', 'medical_name', 'location', 'phone_number']
        labels = {
            'blood_group': 'Blood Group',
            'date_time': 'Time',
            'Disease_name': 'Disease Name',
            'No_of_bag': 'No of Bag',
            'medical_name': 'Medical Name',
            'location': 'Location',
            'phone_number': 'Phone'
        }
        widgets = {
            'blood_group': forms.Select(attrs={'class': 'form-control'}),
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'Disease_name': forms.TextInput(attrs={'class': 'form-control'}),
            'No_of_bag': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Required no of bags'}),
            'medical_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel'})
        }

class UserRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=150, label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    blood_group = forms.ChoiceField(
        choices=[
            ('A+', 'A+'),
            ('A-', 'A-'),
            ('B+', 'B+'),
            ('B-', 'B-'),
            ('AB+', 'AB+'),
            ('AB-', 'AB-'),
            ('O+', 'O+'),
            ('O-', 'O-'),
        ],
        label='Blood Group',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    phone_number = forms.CharField(max_length=15, label='Phone Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(max_length=250, label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_img = forms.ImageField(required=False, label='Image', widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    username = forms.CharField(required=False, label='User Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False, label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(required=False, label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='Leave empty if not changing the password')
    password2 = forms.CharField(required=False, label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text='Leave empty if not changing the password')
    last_blood_donation = forms.DateField(
        label='Last Blood Donation Date',
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        required=False  # Make this optional if desired
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'name', 'blood_group', 'phone_number', 'address', 'profile_img', 'last_blood_donation')

    # Validate email for uniqueness
    def clean_email(self):
        email = self.cleaned_data.get('email')
        # If email exists and doesn't belong to the current user
        if email:
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']  # Save email to the user
            if commit:
                user.save()  # Save the User instance
                user_profile = UserProfile(
                    user=user,
                    name=self.cleaned_data['name'],
                    blood_group=self.cleaned_data['blood_group'],
                    phone_number=self.cleaned_data['phone_number'],
                    address=self.cleaned_data['address'],
                    profile_img=self.cleaned_data.get('profile_img'),
                    last_blood_donation=self.cleaned_data.get('last_blood_donation'),  # Save last blood donation date
                )
                user_profile.save()  # Save the UserProfile instance
            return user




class userLogin(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'})
    )


class RequestPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Enter your email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

class VerifyOTPForm(forms.Form):
    otp = forms.CharField(max_length=6, label="Enter OTP", widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class blogPostform(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))  # Use TinyMCE widget
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        labels = {
            'title': 'Title',
            'content': 'Content',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your blog title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your blog content here...'}),
        }
