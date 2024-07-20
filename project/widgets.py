from django import forms

class UserAutocompleteWidget(forms.TextInput):
    template_name = 'widgets/user_autocomplete.html'

    class Media:
        js = ('js/user_autocomplete.js',)