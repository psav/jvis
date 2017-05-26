from django import forms


class GuiForm(forms.Form):
    source_data = forms.CharField(
        label="Source",
        widget=forms.Textarea
    )
