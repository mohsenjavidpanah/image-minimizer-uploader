from django import forms

from .models import UploadModel


class StoreImageForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = ['upload_file']
