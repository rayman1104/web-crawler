from django import forms


class CrawlActionForm(forms.Form):
    url = forms.URLField()
