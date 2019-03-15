class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['username']