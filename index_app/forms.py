from django import forms


class PhotoForm(forms.Form):
    photo_name = forms.CharField(label="photo name", max_length=13)
    photo = forms.FileField()
