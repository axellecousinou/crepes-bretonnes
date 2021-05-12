from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from datetime import datetime
from .models import Article
from .forms import ContactForm
#from .forms import ArticleForm
from .models import Contact
from .forms import NouveauContactForm
from django.contrib.auth import authenticate, login, logout
from .forms import ConnexionForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes sont bretonnes ça tue des mouettes en plein vol !</p>
        """)


def view_article(request, id_article):
    return HttpResponse("Vous avez demandé l'article numéro {0} !".format(id_article))


def list_articles_by_tag(request, tag):
    if tag == "error":
        raise Http404
    return redirect(view_redirection)


def list_articles(request, month, year):
    return HttpResponse("Vous avez demandé la liste des articles parus au mois de {0} de "
                        "l'année {1}".format(month, year))


def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date':datetime.now()})


def addition(request, nb1, nb2):
    total = nb1 + nb2
    return render(request, 'blog/addition.html', locals())


def accueil(request):
    """Afficher tous les articles de notre blog """
    articles = Article.objects.all() #On sélectionne nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})


def lire(request, id, slug):
    """Afficher un article complet"""
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/lire.html', {'article': article})


def show_image(request):
    return render(request, 'blog/image.html')


def contacts(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoye = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        envoi = True

    return render(request, 'blog/contact.html', locals())


"""
def add_article(request):
    form = ArticleForm(request.POST)

    if form.is_valid():
        article = form.save(commit=False)
        return render(request, 'blog/accueil.html', locals())

    return render(request, 'blog/contact.html', locals())
"""


def nouveau_contact(request):
    sauvegarde = False
    form = NouveauContactForm(request.POST or None, request.FILES)
    if form.is_valid():
        contact = Contact()
        contact.nom = form.cleaned_data["nom"]
        contact.adresse = form.cleaned_data["adresse"]
        contact.photo = form.cleaned_data["photo"]
        contact.save()
        sauvegarde = True
    return render(request, 'blog/cont.html', {
        'form': form, 'sauvegarde': sauvegarde
    })


def voir_contacts(request):
    return render(request, 'blog/voir_contacts.html',
                  {'contacts': Contact.objects.all()})


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(request, 'blog/connexion.html', locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))


@login_required
def ma_vue(request):
    return None
