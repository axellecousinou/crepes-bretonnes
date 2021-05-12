from django import forms
from .models import Article


class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="Cochez si vous souhaitez obtenir une copie du mail envoyé",
                                required=False)

    """
Si jamais notre nettoyage ne dépend que d'un champ à la fois
    def clean_message(self):
        message = self.cleaned_data['message']
        if "pizza" in message:
            raise forms.ValidationError("On ne veut pas entendre parler de pizza")

        return message
    
    """

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message:
            if "pizza" in sujet and "pizza" in message:
                self.add_error("message", "Vous parlez de pizzas dans le sujet "
                                          "ET le message ? Non mais ho ! Daleux va")

        return cleaned_data


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('auteur', 'categorie', 'slug')
        # Equivalent à mettre fields = ('titre', 'contenu')


class NouveauContactForm(forms.Form):
    nom = forms.CharField()
    adresse = forms.CharField(widget=forms.Textarea)
    photo = forms.ImageField()


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
