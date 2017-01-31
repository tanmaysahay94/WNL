from django import forms

class OptionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('options')
        super(OptionForm, self).__init__(*args, **kwargs)
        self.fields['toChoose'] = forms.ChoiceField(choices=options, widget=forms.RadioSelect)

class _OptionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop('options')
        h_words = kwargs.pop('h_words')
        super(_OptionForm, self).__init__(*args, **kwargs)
        self.fields['h_words'] = [h['hindi_word'] for h in h_words]
        self.fields['toChoose'] = forms.ChoiceField(choices=options, widget=forms.RadioSelect)
