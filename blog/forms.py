from django import forms
from .models import BlogUser

class ProfileForm(forms.ModelForm):
    class Meta:
        model = BlogUser
        fields = ['headshot', 'bio']

    headshot = forms.ImageField(label='頭貼',required=False,allow_empty_file=True)
    bio = forms.CharField(label='個人資料', widget=forms.Textarea(attrs={'rows': 5}))
