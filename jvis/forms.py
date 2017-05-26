from django import forms


class GuiForm(forms.Form):
    source_type = forms.ChoiceField(
        label="Source Type",
        widget=forms.Select,
        choices=[('JSON', 'JSON'), ('YAML', 'YAML')]
    )
    source_data = forms.CharField(
        label="Source",
        widget=forms.Textarea
    )
